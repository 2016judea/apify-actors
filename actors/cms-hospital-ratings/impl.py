async def run(inp, client, emit):
    params = {"limit": 500, "offset": 0}
    conds = []
    for k, f in [("state", "state"), ("city", "citytown"), ("hospitalType", "hospital_type"), ("minRating", "hospital_overall_rating")]:
        if inp.get(k):
            conds.append((f, str(inp[k]).upper() if k in ("state", "city") else str(inp[k]), ">=" if k == "minRating" else "="))
    for i, (f, v, op) in enumerate(conds):
        params[f"conditions[{i}][property]"] = f
        params[f"conditions[{i}][value]"] = v
        params[f"conditions[{i}][operator]"] = op
    while True:
        d = await client.json("https://data.cms.gov/provider-data/api/1/datastore/query/xubh-q36u/0", params=params)
        res = d.get("results", [])
        for r in res:
            r = {k: v for k, v in r.items() if v not in ("", None) and not k.endswith("_footnote")}
            r["careCompareUrl"] = f"https://www.medicare.gov/care-compare/details/hospital/{r.get('facility_id')}"
            await emit(r)
        if len(res) < 500:
            return
        params["offset"] += 500
