async def run(inp, client, emit):
    vehicles = inp.get("vehicles") or [{"make": "Tesla", "model": "Model 3", "year": 2022}]
    kw = (inp.get("component") or "").upper()
    for v in vehicles:
        d = await client.json("https://api.nhtsa.gov/complaints/complaintsByVehicle",
                              params={"make": v["make"], "model": v["model"], "modelYear": v["year"]})
        res = sorted(d.get("results", []), key=lambda r: r.get("dateComplaintFiled") or "", reverse=True)
        for r in res:
            if kw and kw not in (r.get("components") or "").upper():
                continue
            prods = r.pop("products", None) or []
            r["vehicle"] = f'{v["year"]} {v["make"]} {v["model"]}'
            r["productCount"] = len(prods)
            await emit(r)
