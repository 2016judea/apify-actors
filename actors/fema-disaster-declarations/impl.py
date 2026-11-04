async def run(inp, client, emit):
    flt = []
    if inp.get("state"):
        flt.append(f"state eq '{inp['state'].upper()}'")
    if inp.get("declaredSince"):
        flt.append(f"declarationDate ge '{inp['declaredSince']}T00:00:00.000Z'")
    if inp.get("incidentType"):
        flt.append(f"incidentType eq '{inp['incidentType']}'")
    params = {"$orderby": "declarationDate desc", "$top": 1000, "$skip": 0}
    if flt:
        params["$filter"] = " and ".join(flt)
    while True:
        d = await client.json("https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries", params=params)
        rows = d.get("DisasterDeclarationsSummaries", [])
        for r in rows:
            for k in ("id", "hash", "lastRefresh"):
                r.pop(k, None)
            await emit(r)
        if len(rows) < 1000:
            return
        params["$skip"] += 1000
