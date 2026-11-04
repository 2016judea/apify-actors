async def run(inp, client, emit):
    q = []
    if inp.get("decidedSince"):
        q.append(f"decision_date:[{inp['decidedSince'].replace('-', '')} TO 29991231]")
    if inp.get("applicant"):
        q.append(f'applicant:"{inp["applicant"]}"')
    if inp.get("deviceName"):
        q.append(f'device_name:"{inp["deviceName"]}"')
    if inp.get("productCode"):
        q.append(f'product_code:{inp["productCode"].upper()}')
    params = {"limit": 100, "skip": 0, "sort": "decision_date:desc"}
    if q:
        params["search"] = " AND ".join(q)
    while params["skip"] < 25000:
        try:
            d = await client.json("https://api.fda.gov/device/510k.json", params=params)
        except Exception as e:
            if "404" in str(e):
                return
            raise
        res = d.get("results", [])
        for r in res:
            of = r.pop("openfda", {}) or {}
            r["deviceClass"] = of.get("device_class")
            r["medicalSpecialty"] = of.get("medical_specialty_description")
            r["regulationNumber"] = of.get("regulation_number")
            r["url"] = f"https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID={r.get('k_number')}"
            await emit(r)
        if len(res) < 100:
            return
        params["skip"] += 100
