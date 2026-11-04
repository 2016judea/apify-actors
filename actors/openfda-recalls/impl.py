async def run(inp, client, emit):
    kind = inp.get("productType") or "food"
    q = []
    if inp.get("reportedSince"):
        q.append(f"report_date:[{inp['reportedSince'].replace('-', '')} TO 29991231]")
    if inp.get("classification"):
        q.append(f'classification:"{inp["classification"]}"')
    if inp.get("state"):
        q.append(f'state:"{inp["state"].upper()}"')
    if inp.get("firm"):
        q.append(f'recalling_firm:"{inp["firm"]}"')
    if inp.get("keyword"):
        q.append(f'(product_description:"{inp["keyword"]}" OR reason_for_recall:"{inp["keyword"]}")')
    params = {"limit": 100, "skip": 0, "sort": "report_date:desc"}
    if q:
        params["search"] = " AND ".join(q)
    while params["skip"] < 25000:
        try:
            d = await client.json(f"https://api.fda.gov/{kind}/enforcement.json", params=params)
        except Exception as e:
            if "404" in str(e):
                return
            raise
        res = d.get("results", [])
        for r in res:
            r.pop("openfda", None)
            r["productType"] = kind
            await emit(r)
        if len(res) < 100:
            return
        params["skip"] += 100
