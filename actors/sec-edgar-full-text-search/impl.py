H = {"User-Agent": "cheerful_term apify actor aidan@brickandmortar.dev"}


async def run(inp, client, emit):
    params = {"q": inp.get("query") or '"going concern"'}
    if inp.get("forms"):
        params["forms"] = inp["forms"]
    if inp.get("startDate") or inp.get("endDate"):
        params["dateRange"] = "custom"
        params["startdt"] = inp.get("startDate") or "2001-01-01"
        params["enddt"] = inp.get("endDate") or "2099-12-31"
    frm = 0
    while True:
        params["from"] = frm
        d = await client.json("https://efts.sec.gov/LATEST/search-index", params=params, headers=H)
        hits = d.get("hits", {}).get("hits", [])
        if not hits:
            return
        for h in hits:
            s = h.get("_source", {})
            adsh, _, fname = h["_id"].partition(":")
            cik = (s.get("ciks") or [""])[0].lstrip("0")
            await emit({
                "companies": s.get("display_names"), "ciks": s.get("ciks"), "form": s.get("form"),
                "rootForms": s.get("root_forms"), "filingDate": s.get("file_date"), "periodEnding": s.get("period_ending"),
                "fileType": s.get("file_type"), "fileDescription": s.get("file_description"), "accessionNumber": adsh,
                "sics": s.get("sics"), "bizStates": s.get("biz_states"), "incStates": s.get("inc_states"),
                "documentUrl": f"https://www.sec.gov/Archives/edgar/data/{cik}/{adsh.replace('-', '')}/{fname}" if cik else None,
            })
        frm += len(hits)
        if frm >= min(d.get("hits", {}).get("total", {}).get("value", 0), 10000):
            return
