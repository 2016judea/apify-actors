"""Look up comparable Store actors and their per-result price.

    .venv/bin/python scripts/price.py "building permits" ["second query"...]

Prints the top 3 actors (by total users) that charge per result, their
per-result price, and the median. Per-result means the primary PPE event, or
the PRICE_PER_DATASET_ITEM unit price. Monthly-rental actors are skipped.
"""
import statistics
import sys

import httpx


def per_result(info):
    if not info:
        return None
    m = info.get("pricingModel")
    if m == "PRICE_PER_DATASET_ITEM":
        return info.get("pricePerUnitUsd")
    if m == "PAY_PER_EVENT":
        ev = (info.get("pricingPerEvent") or {}).get("actorChargeEvents") or {}
        cands = [(k, v) for k, v in ev.items() if k != "apify-actor-start" and v.get("eventPriceUsd")]
        prim = [v for k, v in cands if v.get("isPrimaryEvent")] or [v for k, v in cands if k == "apify-default-dataset-item"] or [v for k, v in cands]
        if prim:
            return prim[0]["eventPriceUsd"]
    return None


def lookup(queries):
    seen = {}
    for q in queries:
        d = httpx.get("https://api.apify.com/v2/store", params={"search": q, "limit": 40}, timeout=60).json()["data"]["items"]
        for i in d:
            p = per_result(i.get("currentPricingInfo"))
            if p and p < 1:
                seen[i["username"] + "/" + i["name"]] = (i.get("stats", {}).get("totalUsers", 0), p)
    top = sorted(seen.items(), key=lambda kv: -kv[1][0])[:3]
    return top


if __name__ == "__main__":
    top = lookup(sys.argv[1:])
    for k, (u, p) in top:
        print(f"{k}\tusers={u}\t${p}")
    if top:
        print("MEDIAN", statistics.median(p for _, (u, p) in top))
        print("CELL", "; ".join(f"{k} ${p}" for k, (u, p) in top))
