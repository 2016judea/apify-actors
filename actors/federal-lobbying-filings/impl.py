async def run(inp, client, emit):
    params = {"page_size": 25, "ordering": "-dt_posted"}
    for k, a in [("clientName", "client_name"), ("registrantName", "registrant_name"), ("filingYear", "filing_year"),
                 ("issueCode", "filing_specific_lobbying_issues"), ("governmentEntity", "lobbyist_conviction_disclosure")]:
        if inp.get(k) and k != "governmentEntity":
            params[a] = inp[k]
    url = "https://lda.gov/api/v1/filings/"
    while url:
        d = await client.json(url, params=params)
        params = None
        for f in d.get("results", []):
            acts = f.get("lobbying_activities") or []
            await emit({
                "filingUuid": f.get("filing_uuid"), "filingType": f.get("filing_type_display"), "filingYear": f.get("filing_year"),
                "period": f.get("filing_period_display"), "posted": f.get("dt_posted"), "income": f.get("income"), "expenses": f.get("expenses"),
                "registrant": (f.get("registrant") or {}).get("name"), "client": (f.get("client") or {}).get("name"),
                "clientState": (f.get("client") or {}).get("state"), "clientDescription": (f.get("client") or {}).get("general_description"),
                "issues": [a.get("general_issue_code_display") for a in acts],
                "specificIssues": [a.get("description") for a in acts],
                "governmentEntities": sorted({g.get("name") for a in acts for g in a.get("government_entities") or []}),
                "lobbyists": sorted({" ".join(x for x in [(l.get("lobbyist") or {}).get("first_name"), (l.get("lobbyist") or {}).get("last_name")] if x) for a in acts for l in a.get("lobbyists") or []}),
                "documentUrl": f.get("filing_document_url"),
            })
        url = d.get("next")
