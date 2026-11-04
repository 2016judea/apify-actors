async def run(inp, client, emit):
    params = {"output": "JSON", "p_act": "Y" if inp.get("activeOnly", True) else "N"}
    for k, a in [("state", "p_st"), ("city", "p_ct"), ("zip", "p_zip"), ("name", "p_fn"), ("naics", "p_ncs")]:
        if inp.get(k):
            params[a] = inp[k]
    if inp.get("withViolationsOnly"):
        params["p_qiv"] = "GT0"
    if inp.get("withPenaltiesOnly"):
        params["p_pen"] = "GT0"
    d = await client.json("https://echodata.epa.gov/echo/echo_rest_services.get_facilities", params=params)
    qid = d["Results"].get("QueryID")
    if not qid:
        return
    page = 1
    while True:
        d = await client.json("https://echodata.epa.gov/echo/echo_rest_services.get_qid",
                              params={"qid": qid, "pageno": page, "output": "JSON"})
        fac = d.get("Results", {}).get("Facilities", []) or []
        for f in fac:
            f = {k: v for k, v in f.items() if v not in (None, "", " ")}
            if f.get("RegistryID"):
                f["echoUrl"] = f"https://echo.epa.gov/detailed-facility-report?fid={f['RegistryID']}"
            await emit(f)
        if not fac:
            return
        page += 1
