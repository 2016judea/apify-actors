async def run(inp, client, emit):
    params = {"pageSize": 100, "format": "json"}
    if inp.get("condition"):
        params["query.cond"] = inp["condition"]
    if inp.get("intervention"):
        params["query.intr"] = inp["intervention"]
    if inp.get("sponsor"):
        params["query.spons"] = inp["sponsor"]
    if inp.get("location"):
        params["query.locn"] = inp["location"]
    if inp.get("status"):
        params["filter.overallStatus"] = inp["status"]
    while True:
        d = await client.json("https://clinicaltrials.gov/api/v2/studies", params=params)
        for st in d.get("studies", []):
            p = st.get("protocolSection", {})
            idm, sm, de = p.get("identificationModule", {}), p.get("statusModule", {}), p.get("designModule", {})
            sp = p.get("sponsorCollaboratorsModule", {})
            locs = (p.get("contactsLocationsModule", {}) or {}).get("locations", []) or []
            await emit({
                "nctId": idm.get("nctId"), "title": idm.get("briefTitle"), "officialTitle": idm.get("officialTitle"),
                "status": sm.get("overallStatus"), "startDate": (sm.get("startDateStruct") or {}).get("date"),
                "primaryCompletion": (sm.get("primaryCompletionDateStruct") or {}).get("date"),
                "lastUpdate": (sm.get("lastUpdatePostDateStruct") or {}).get("date"),
                "phases": de.get("phases"), "studyType": de.get("studyType"),
                "enrollment": (de.get("enrollmentInfo") or {}).get("count"),
                "conditions": (p.get("conditionsModule") or {}).get("conditions"),
                "interventions": [i.get("name") for i in (p.get("armsInterventionsModule") or {}).get("interventions", []) or []],
                "leadSponsor": (sp.get("leadSponsor") or {}).get("name"),
                "sponsorClass": (sp.get("leadSponsor") or {}).get("class"),
                "collaborators": [c.get("name") for c in sp.get("collaborators", []) or []],
                "locationCount": len(locs),
                "locations": [", ".join(x for x in [l.get("facility"), l.get("city"), l.get("state"), l.get("country")] if x) for l in locs[:25]],
                "summary": (p.get("descriptionModule") or {}).get("briefSummary"),
                "url": f"https://clinicaltrials.gov/study/{idm.get('nctId')}",
            })
        tok = d.get("nextPageToken")
        if not tok:
            return
        params["pageToken"] = tok
