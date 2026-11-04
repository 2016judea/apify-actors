async def run(inp, client, emit):
    vehicles = inp.get("vehicles") or [{"make": "Honda", "model": "Civic", "year": 2020}]
    for v in vehicles:
        d = await client.json("https://api.nhtsa.gov/recalls/recallsByVehicle",
                              params={"make": v["make"], "model": v["model"], "modelYear": v["year"]})
        for r in d.get("results", []):
            r["query"] = f'{v["year"]} {v["make"]} {v["model"]}'
            r["url"] = f"https://www.nhtsa.gov/recalls?nhtsaId={r.get('NHTSACampaignNumber')}"
            await emit(r)
