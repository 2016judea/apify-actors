from .lib import Client

H = {"User-Agent": "cheerful_term apify actor aidan@brickandmortar.dev"}


async def cik_for(client, q):
    q = str(q).strip()
    if q.isdigit():
        return int(q)
    d = await client.json("https://www.sec.gov/files/company_tickers.json", headers=H)
    for v in d.values():
        if v["ticker"].upper() == q.upper() or v["title"].upper() == q.upper():
            return int(v["cik_str"])
    for v in d.values():
        if q.upper() in v["title"].upper():
            return int(v["cik_str"])
    raise ValueError(f"No SEC registrant found for {q!r}")


async def run(inp, client, emit):
    forms = {f.strip().upper() for f in (inp.get("forms") or "").split(",") if f.strip()}
    since = inp.get("filedSince") or ""
    for comp in inp.get("companies") or ["AAPL"]:
        cik = await cik_for(client, comp)
        d = await client.json(f"https://data.sec.gov/submissions/CIK{cik:010d}.json", headers=H)
        rec = d["filings"]["recent"]
        n = len(rec["accessionNumber"])
        for i in range(n):
            form = rec["form"][i]
            if forms and form.upper() not in forms:
                continue
            if since and rec["filingDate"][i] < since:
                continue
            acc = rec["accessionNumber"][i]
            doc = rec["primaryDocument"][i]
            base = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}"
            await emit({
                "company": d.get("name"), "cik": cik, "tickers": d.get("tickers"), "form": form,
                "filingDate": rec["filingDate"][i], "reportDate": rec["reportDate"][i] or None,
                "acceptanceDateTime": rec["acceptanceDateTime"][i], "accessionNumber": acc,
                "description": rec["primaryDocDescription"][i] or None, "items": rec["items"][i] or None,
                "size": rec["size"][i], "documentUrl": f"{base}/{doc}" if doc else None,
                "indexUrl": f"{base}/{acc}-index.htm", "sic": d.get("sic"), "sicDescription": d.get("sicDescription"),
                "stateOfIncorporation": d.get("stateOfIncorporation"),
            })
