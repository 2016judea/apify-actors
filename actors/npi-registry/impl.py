from .lib import compact


def flat(r):
    b = r.get("basic", {})
    loc = next((a for a in r.get("addresses", []) if a.get("address_purpose") == "LOCATION"), {})
    tax = next((t for t in r.get("taxonomies", []) if t.get("primary")), (r.get("taxonomies") or [{}])[0])
    name = b.get("organization_name") or " ".join(x for x in [b.get("first_name"), b.get("middle_name"), b.get("last_name")] if x)
    return compact({
        "npi": r.get("number"), "type": "Organization" if r.get("enumeration_type") == "NPI-2" else "Individual",
        "name": name, "credential": b.get("credential"), "status": b.get("status"),
        "enumerationDate": b.get("enumeration_date"), "lastUpdated": b.get("last_updated"),
        "authorizedOfficial": " ".join(x for x in [b.get("authorized_official_first_name"), b.get("authorized_official_last_name")] if x) or None,
        "authorizedOfficialTitle": b.get("authorized_official_title_or_position"),
        "primaryTaxonomy": tax.get("desc"), "taxonomyCode": tax.get("code"), "licenseState": tax.get("state"),
        "address": loc.get("address_1"), "address2": loc.get("address_2"), "city": loc.get("city"), "state": loc.get("state"),
        "zip": (loc.get("postal_code") or "")[:5], "phone": loc.get("telephone_number"),
        "otherTaxonomies": [t.get("desc") for t in r.get("taxonomies", []) if not t.get("primary")],
    })


async def run(inp, client, emit):
    params = {"version": "2.1", "limit": 200}
    for k_in, k_api in [("taxonomy", "taxonomy_description"), ("city", "city"), ("state", "state"), ("zip", "postal_code"),
                        ("organizationName", "organization_name"), ("lastName", "last_name"), ("firstName", "first_name"),
                        ("npi", "number")]:
        if inp.get(k_in):
            params[k_api] = inp[k_in]
    if inp.get("providerType") in ("NPI-1", "NPI-2"):
        params["enumeration_type"] = inp["providerType"]
    skip = 0
    while skip <= 1000:  # the NPPES API stops at skip 1000
        params["skip"] = skip
        d = await client.json("https://npiregistry.cms.hhs.gov/api/", params=params)
        res = d.get("results") or []
        for r in res:
            await emit(flat(r))
        if len(res) < 200:
            return
        skip += 200
