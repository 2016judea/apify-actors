import re
import xml.etree.ElementTree as ET

H = {"User-Agent": "cheerful_term apify actor aidan@brickandmortar.dev"}
CODES = {"P": "Open-market purchase", "S": "Open-market sale", "A": "Grant/award", "M": "Option exercise",
         "F": "Tax withholding", "G": "Gift", "D": "Disposition to issuer", "C": "Conversion", "X": "Option exercise (in the money)"}


def t(el, path):
    x = el.find(path)
    return x.text.strip() if x is not None and x.text else None


async def cik_for(client, q):
    q = str(q).strip()
    if q.isdigit():
        return int(q)
    d = await client.json("https://www.sec.gov/files/company_tickers.json", headers=H)
    for v in d.values():
        if v["ticker"].upper() == q.upper():
            return int(v["cik_str"])
    raise ValueError(f"Unknown ticker {q!r}")


async def run(inp, client, emit):
    since = inp.get("filedSince") or ""
    only_open_market = bool(inp.get("openMarketOnly"))
    for tk in inp.get("tickers") or ["NVDA"]:
        cik = await cik_for(client, tk)
        d = await client.json(f"https://data.sec.gov/submissions/CIK{cik:010d}.json", headers=H)
        rec = d["filings"]["recent"]
        for i, form in enumerate(rec["form"]):
            if form not in ("4", "4/A"):
                continue
            if since and rec["filingDate"][i] < since:
                break
            acc = rec["accessionNumber"][i]
            doc = re.sub(r"^xslF345X\d+/", "", rec["primaryDocument"][i])
            url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{doc}"
            try:
                root = ET.fromstring((await client.get(url, headers=H)).text)
            except Exception:
                continue
            owners = [{"name": t(o, "reportingOwnerId/rptOwnerName"),
                       "isDirector": t(o, "reportingOwnerRelationship/isDirector"),
                       "isOfficer": t(o, "reportingOwnerRelationship/isOfficer"),
                       "officerTitle": t(o, "reportingOwnerRelationship/officerTitle"),
                       "isTenPercentOwner": t(o, "reportingOwnerRelationship/isTenPercentOwner")}
                      for o in root.findall("reportingOwner")]
            for tx in root.findall("nonDerivativeTable/nonDerivativeTransaction"):
                code = t(tx, "transactionCoding/transactionCode")
                if only_open_market and code not in ("P", "S"):
                    continue
                sh = t(tx, "transactionAmounts/transactionShares/value")
                px = t(tx, "transactionAmounts/transactionPricePerShare/value")
                await emit({
                    "ticker": tk.upper(), "issuer": t(root, "issuer/issuerName"), "filingDate": rec["filingDate"][i],
                    "insider": owners[0]["name"] if owners else None,
                    "role": (owners[0]["officerTitle"] or ("Director" if owners[0]["isDirector"] in ("1", "true") else None)) if owners else None,
                    "transactionDate": t(tx, "transactionDate/value"), "security": t(tx, "securityTitle/value"),
                    "code": code, "codeMeaning": CODES.get(code),
                    "acquiredDisposed": t(tx, "transactionAmounts/transactionAcquiredDisposedCode/value"),
                    "shares": float(sh) if sh else None, "pricePerShare": float(px) if px else None,
                    "value": round(float(sh) * float(px), 2) if sh and px else None,
                    "sharesOwnedAfter": float(t(tx, "postTransactionAmounts/sharesOwnedFollowingTransaction/value") or 0) or None,
                    "directOrIndirect": t(tx, "ownershipNature/directOrIndirectOwnership/value"),
                    "accessionNumber": acc, "url": url, "owners": owners,
                })
