from .lib import compact

URL = "https://api.usaspending.gov/api/v2/search/spending_by_award/"
TYPES = {
    "contracts": ["A", "B", "C", "D"],
    "grants": ["02", "03", "04", "05"],
    "loans": ["07", "08"],
    "direct_payments": ["06", "10"],
    "idvs": ["IDV_A", "IDV_B", "IDV_B_A", "IDV_B_B", "IDV_B_C", "IDV_C", "IDV_D", "IDV_E"],
}
FIELDS = {
    "contracts": ["Award ID", "Recipient Name", "Recipient UEI", "Award Amount", "Total Outlays", "Description",
                  "Start Date", "End Date", "Awarding Agency", "Awarding Sub Agency", "Funding Agency",
                  "Contract Award Type", "NAICS", "PSC", "Place of Performance State Code",
                  "Place of Performance City Code", "Place of Performance Zip5", "Last Modified Date", "generated_internal_id"],
    "grants": ["Award ID", "Recipient Name", "Recipient UEI", "Award Amount", "Total Outlays", "Description",
               "Start Date", "End Date", "Awarding Agency", "Awarding Sub Agency", "Award Type", "CFDA Number",
               "Assistance Listings", "Place of Performance State Code", "Place of Performance Zip5",
               "Last Modified Date", "generated_internal_id"],
}


async def run(inp, client, emit):
    kind = inp.get("awardType") or "contracts"
    f = {"award_type_codes": TYPES[kind],
         "time_period": [{"start_date": inp.get("startDate") or "2025-10-01",
                          "end_date": inp.get("endDate") or "2099-12-31"}]}
    if inp.get("keywords"):
        f["keywords"] = [k.strip() for k in inp["keywords"].split(",") if k.strip()]
    if inp.get("recipient"):
        f["recipient_search_text"] = [inp["recipient"]]
    if inp.get("agency"):
        f["agencies"] = [{"type": "awarding", "tier": "toptier", "name": inp["agency"]}]
    if inp.get("naics"):
        f["naics_codes"] = [x.strip() for x in str(inp["naics"]).split(",") if x.strip()]
    if inp.get("state"):
        f["place_of_performance_locations"] = [{"country": "USA", "state": inp["state"].upper()}]
    if inp.get("minAmount"):
        f["award_amounts"] = [{"lower_bound": float(inp["minAmount"])}]
    fields = FIELDS.get(kind, FIELDS["grants"])
    page = 1
    while True:
        body = {"filters": f, "fields": fields, "page": page, "limit": 100, "sort": "Award Amount", "order": "desc",
                "subawards": False}
        r = await client.post(URL, json=body)
        d = r.json()
        for row in d.get("results", []):
            row = compact(row)
            gid = row.pop("generated_internal_id", None)
            if gid:
                row["url"] = f"https://www.usaspending.gov/award/{gid}"
            row.pop("internal_id", None)
            await emit(row)
        if not d.get("page_metadata", {}).get("hasNext"):
            return
        page += 1
