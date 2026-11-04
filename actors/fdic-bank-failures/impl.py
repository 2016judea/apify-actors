async def run(inp, client, emit):
    f = []
    if inp.get("state"):
        f.append(f'PSTALP:{inp["state"].upper()}')
    if inp.get("failedSince"):
        f.append(f'FAILDATE:["{inp["failedSince"]}" TO *]')
    params = {"fields": "NAME,CERT,FIN,CITYST,PSTALP,FAILDATE,SAVR,RESTYPE,RESTYPE1,QBFASSET,QBFDEP,COST,CHCLASS1",
              "sort_by": "FAILDATE", "sort_order": "DESC", "limit": 1000, "offset": 0}
    if f:
        params["filters"] = " AND ".join(f)
    while True:
        d = await client.json("https://api.fdic.gov/banks/failures", params=params)
        data = d.get("data", [])
        for x in data:
            r = x["data"]
            r.pop("ID", None)
            await emit(r)
        params["offset"] += len(data)
        if not data or params["offset"] >= d.get("meta", {}).get("total", 0):
            return
