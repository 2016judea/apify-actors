async def run(inp, client, emit):
    body = {"rows": 100, "startRecordNum": 0, "oppStatuses": inp.get("status") or "forecasted|posted"}
    if inp.get("keyword"):
        body["keyword"] = inp["keyword"]
    if inp.get("agency"):
        body["agencies"] = inp["agency"]
    if inp.get("eligibility"):
        body["eligibilities"] = inp["eligibility"]
    if inp.get("category"):
        body["fundingCategories"] = inp["category"]
    while True:
        r = await client.post("https://api.grants.gov/v1/api/search2", json=body)
        d = r.json().get("data", {})
        hits = d.get("oppHits", [])
        for h in hits:
            h["url"] = f"https://www.grants.gov/search-results-detail/{h.get('id')}"
            await emit(h)
        body["startRecordNum"] += len(hits)
        if not hits or body["startRecordNum"] >= d.get("hitCount", 0):
            return
