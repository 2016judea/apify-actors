H = {"User-Agent": "cheerful_term apify actor aidan@brickandmortar.dev"}
CONCEPTS = {
    "revenue": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"],
    "netIncome": ["NetIncomeLoss"], "operatingIncome": ["OperatingIncomeLoss"], "grossProfit": ["GrossProfit"],
    "eps": ["EarningsPerShareDiluted"], "totalAssets": ["Assets"], "totalLiabilities": ["Liabilities"],
    "equity": ["StockholdersEquity"], "cash": ["CashAndCashEquivalentsAtCarryingValue"],
    "operatingCashFlow": ["NetCashProvidedByUsedInOperatingActivities"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment"], "longTermDebt": ["LongTermDebtNoncurrent", "LongTermDebt"],
    "sharesOutstanding": ["CommonStockSharesOutstanding", "EntityCommonStockSharesOutstanding"],
}


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
    period = (inp.get("period") or "annual").lower()
    years = int(inp.get("years") or 5)
    for tk in inp.get("tickers") or ["MSFT"]:
        cik = await cik_for(client, tk)
        d = await client.json(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json", headers=H)
        facts = {**d["facts"].get("us-gaap", {}), **d["facts"].get("dei", {})}
        rows = {}
        for key, names in CONCEPTS.items():
            for nm in names:
                if nm not in facts:
                    continue
                for unit, vals in facts[nm]["units"].items():
                    for v in vals:
                        # Only values reported in the period's own primary filing (10-K / 10-Q), not restated comparatives
                        if period == "annual" and (v.get("form") not in ("10-K", "10-K/A", "20-F", "40-F") or v.get("fp") != "FY"):
                            continue
                        if period == "quarterly" and v.get("form") not in ("10-Q", "10-Q/A"):
                            continue
                        if "start" in v and period == "quarterly":
                            from datetime import date
                            s, e = date.fromisoformat(v["start"]), date.fromisoformat(v["end"])
                            if not 80 <= (e - s).days <= 100:
                                continue
                        if "start" in v and period == "annual":
                            from datetime import date
                            s, e = date.fromisoformat(v["start"]), date.fromisoformat(v["end"])
                            if not 350 <= (e - s).days <= 380:
                                continue
                        if "start" not in v and v["end"] not in rows:
                            continue  # balance-sheet/cover values attach only to a reported period end
                        r = rows.setdefault(v["end"], {"ticker": tk.upper(), "company": d.get("entityName"), "cik": cik,
                                                       "periodEnd": v["end"], "period": period})
                        if key not in r:
                            r[key] = v["val"]
                            r.setdefault("filed", v.get("filed"))
                            r.setdefault("form", v.get("form"))
                            r.setdefault("fiscalYear", v.get("fy"))
        for end in sorted(rows, reverse=True)[: years if period == "annual" else years * 4]:
            await emit(rows[end])
