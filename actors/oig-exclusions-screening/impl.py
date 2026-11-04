import csv
import io
import re

CODES = {"1128a1": "Program-related conviction", "1128a2": "Patient abuse/neglect", "1128a3": "Felony health care fraud",
         "1128a4": "Felony controlled substance", "1128b4": "License revocation/suspension", "1128b7": "Fraud, kickbacks",
         "1128b8": "Entity controlled by sanctioned individual", "1128b14": "Default on health education loan", "1128b5": "Excluded from another program"}


def n(s):
    return re.sub(r"[^A-Z0-9]", "", (s or "").upper())


async def run(inp, client, emit):
    r = await client.get("https://oig.hhs.gov/exclusions/downloadables/UPDATED.csv", headers={"Accept": "text/csv"})
    rows = list(csv.DictReader(io.StringIO(r.text)))
    qs = [q.strip() for q in (inp.get("queries") or []) if q.strip()]
    state = (inp.get("state") or "").upper()
    since = (inp.get("excludedSince") or "").replace("-", "")

    def out(x):
        return {
            "name": x["BUSNAME"] or " ".join(p for p in [x["FIRSTNAME"], x["MIDNAME"], x["LASTNAME"]] if p),
            "isBusiness": bool(x["BUSNAME"]), "general": x["GENERAL"], "specialty": x["SPECIALTY"],
            "npi": x["NPI"] if x["NPI"] and x["NPI"] != "0000000000" else None, "address": x["ADDRESS"], "city": x["CITY"],
            "state": x["STATE"], "zip": x["ZIP"], "exclusionType": x["EXCLTYPE"], "exclusionReason": CODES.get(x["EXCLTYPE"].strip().lower()),
            "exclusionDate": x["EXCLDATE"], "reinstatementDate": x["REINDATE"] if x["REINDATE"] != "00000000" else None,
            "waiverDate": x["WAIVERDATE"] if x["WAIVERDATE"] != "00000000" else None,
        }

    if qs:
        for q in qs:
            nq = n(q)
            hits = []
            for x in rows:
                if nq.isdigit() and len(nq) == 10:
                    ok = x["NPI"] == nq
                else:
                    full = n(x["BUSNAME"]) if x["BUSNAME"] else n(x["FIRSTNAME"] + x["LASTNAME"])
                    rev = n(x["LASTNAME"] + x["FIRSTNAME"])
                    ok = bool(full) and (nq == full or nq == rev or (len(nq) > 6 and nq in full))
                if ok and (not state or x["STATE"] == state):
                    hits.append(out(x))
            await emit({"query": q, "isExcluded": bool(hits), "matches": hits[:20],
                        "listSource": "HHS-OIG LEIE UPDATED.csv, fetched at run time"})
        return
    sel = [x for x in rows if (not state or x["STATE"] == state) and (not since or x["EXCLDATE"] >= since)]
    sel.sort(key=lambda x: x["EXCLDATE"], reverse=True)
    for x in sel:
        await emit(out(x))
