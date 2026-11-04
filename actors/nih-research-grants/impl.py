async def run(inp, client, emit):
    crit = {}
    if inp.get("text"):
        crit["advanced_text_search"] = {"operator": "and", "search_field": "projecttitle,terms,abstracttext", "search_text": inp["text"]}
    if inp.get("fiscalYears"):
        crit["fiscal_years"] = [int(y) for y in str(inp["fiscalYears"]).split(",") if y.strip()]
    if inp.get("orgState"):
        crit["org_states"] = [inp["orgState"].upper()]
    if inp.get("orgName"):
        crit["org_names"] = [inp["orgName"]]
    if inp.get("piName"):
        crit["pi_names"] = [{"any_name": inp["piName"]}]
    offset = 0
    while offset < 14999:
        body = {"criteria": crit, "offset": offset, "limit": 500, "sort_field": "award_amount", "sort_order": "desc"}
        r = await client.post("https://api.reporter.nih.gov/v2/projects/search", json=body)
        d = r.json()
        res = d.get("results", [])
        for p in res:
            org = p.get("organization") or {}
            await emit({
                "projectNumber": p.get("project_num"), "title": p.get("project_title"), "fiscalYear": p.get("fiscal_year"),
                "awardAmount": p.get("award_amount"), "directCost": p.get("direct_cost_amt"), "indirectCost": p.get("indirect_cost_amt"),
                "organization": org.get("org_name"), "orgCity": org.get("org_city"), "orgState": org.get("org_state"),
                "principalInvestigators": [x.get("full_name") for x in p.get("principal_investigators") or []],
                "agency": (p.get("agency_ic_admin") or {}).get("name"), "activityCode": p.get("activity_code"),
                "projectStart": p.get("project_start_date"), "projectEnd": p.get("project_end_date"),
                "budgetStart": p.get("budget_start"), "budgetEnd": p.get("budget_end"),
                "abstract": p.get("abstract_text"), "terms": p.get("pref_terms"),
                "url": f"https://reporter.nih.gov/project-details/{p.get('appl_id')}",
            })
        offset += len(res)
        if not res or offset >= d.get("meta", {}).get("total", 0):
            return
