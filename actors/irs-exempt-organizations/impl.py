import csv
import io

NTEE_MAJOR = {"A": "Arts", "B": "Education", "C": "Environment", "D": "Animals", "E": "Health", "F": "Mental health",
              "G": "Disease/disorders", "H": "Medical research", "I": "Crime/legal", "J": "Employment", "K": "Food/agriculture",
              "L": "Housing", "M": "Public safety", "N": "Recreation/sports", "O": "Youth development", "P": "Human services",
              "Q": "International", "R": "Civil rights", "S": "Community improvement", "T": "Philanthropy/grantmaking",
              "U": "Science/technology", "V": "Social science", "W": "Public benefit", "X": "Religion", "Y": "Mutual benefit", "Z": "Unknown"}
FOUNDATION = {"00": "Not a 501(c)(3)", "02": "Private operating foundation (exempt)", "03": "Private operating foundation",
              "04": "Private non-operating foundation", "10": "Church", "11": "School", "12": "Hospital",
              "15": "Publicly supported (gov/public)", "16": "Publicly supported (gross receipts)", "17": "Supporting org (Type I)",
              "21": "Supporting org"}


async def run(inp, client, emit):
    state = (inp.get("state") or "MN").lower()
    r = await client.get(f"https://www.irs.gov/pub/irs-soi/eo_{state}.csv", headers={"Accept": "text/csv"})
    rows = list(csv.DictReader(io.StringIO(r.text)))
    name = (inp.get("name") or "").upper()
    city = (inp.get("city") or "").upper()
    ntee = (inp.get("nteePrefix") or "").upper()
    min_rev = float(inp.get("minRevenue") or 0)
    fonly = bool(inp.get("privateFoundationsOnly"))
    out = []
    for x in rows:
        if name and name not in x["NAME"]:
            continue
        if city and x["CITY"] != city:
            continue
        if ntee and not x["NTEE_CD"].startswith(ntee):
            continue
        rev = float(x["REVENUE_AMT"] or 0)
        if rev < min_rev:
            continue
        if fonly and x["FOUNDATION"] not in ("02", "03", "04"):
            continue
        out.append((rev, x))
    out.sort(key=lambda t: -t[0])
    for rev, x in out:
        await emit({
            "ein": x["EIN"], "name": x["NAME"], "inCareOf": x["ICO"] or None, "street": x["STREET"], "city": x["CITY"],
            "state": x["STATE"], "zip": x["ZIP"], "subsection": "501(c)(" + str(int(x["SUBSECTION"])) + ")" if x["SUBSECTION"].isdigit() else x["SUBSECTION"],
            "foundationCode": x["FOUNDATION"], "foundationType": FOUNDATION.get(x["FOUNDATION"]),
            "nteeCode": x["NTEE_CD"] or None, "nteeCategory": NTEE_MAJOR.get(x["NTEE_CD"][:1]) if x["NTEE_CD"] else None,
            "rulingYear": x["RULING"][:4] or None, "taxPeriod": x["TAX_PERIOD"] or None,
            "assets": float(x["ASSET_AMT"] or 0), "income": float(x["INCOME_AMT"] or 0), "revenue": rev,
            "deductible": x["DEDUCTIBILITY"] == "1",
            "irsLookup": f"https://apps.irs.gov/app/eos/details/?ein={x['EIN']}",
        })
