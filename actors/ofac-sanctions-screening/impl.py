import csv
import difflib
import io
import re

BASE = "https://sanctionslistservice.ofac.treas.gov/api/publicationpreview/exports/"


def norm(s):
    s = re.sub(r"[^A-Z0-9 ]", " ", (s or "").upper())
    s = re.sub(r"\b(LLC|LTD|INC|CO|CORP|COMPANY|LIMITED|THE|OF|SA|JSC|OOO|PJSC|GMBH)\b", " ", s)
    return " ".join(sorted(s.split()))


def score(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()


async def run(inp, client, emit):
    names = [n.strip() for n in (inp.get("names") or []) if n.strip()]
    thr = float(inp.get("minScore") or 0.85)
    sdn = list(csv.reader(io.StringIO((await client.get(BASE + "sdn.csv", headers={"Accept": "text/csv"})).text)))
    alt = list(csv.reader(io.StringIO((await client.get(BASE + "alt.csv", headers={"Accept": "text/csv"})).text)))
    ents = {}
    for r in sdn:
        if len(r) < 4 or not r[0].strip().isdigit():
            continue
        ents[r[0]] = {"uid": int(r[0]), "name": r[1], "type": r[2].replace("-0-", "").strip() or "entity",
                      "programs": r[3], "remarks": r[11].replace("-0-", "").strip() if len(r) > 11 else ""}
    cands = [(norm(e["name"]), e["name"], e) for e in ents.values()]
    for r in alt:
        if len(r) >= 4 and r[0] in ents:
            cands.append((norm(r[3]), r[3], ents[r[0]]))
    for q in names:
        nq = norm(q)
        hits = {}
        for n, raw, e in cands:
            if not n or abs(len(n) - len(nq)) > max(8, len(nq)):
                continue
            sc = score(nq, n)
            if sc >= thr and sc > hits.get(e["uid"], (0,))[0]:
                hits[e["uid"]] = (sc, raw, e)
        top = sorted(hits.values(), key=lambda t: -t[0])[:5]
        await emit({
            "query": q, "isPotentialMatch": bool(top), "bestScore": round(top[0][0], 3) if top else 0,
            "matches": [{"score": round(sc, 3), "matchedName": raw, "sdnName": e["name"], "uid": e["uid"], "type": e["type"],
                         "programs": e["programs"], "remarks": e["remarks"][:500]} for sc, raw, e in top],
            "listSource": "OFAC SDN + aliases (sanctionslistservice.ofac.treas.gov), fetched at run time",
        })
