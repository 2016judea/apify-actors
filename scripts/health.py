"""Clear Apify's UNDER_MAINTENANCE flag once an actor works again.

    .venv/bin/python scripts/health.py        (launchd runs it from publish_all.sh, twice a day)

Apify's daily auto-test runs each public actor's prefill input; when it fails, the
actor gets `notice: UNDER_MAINTENANCE` and Store users see a warning. It is
deprecated after 30 days broken. The flag never clears itself, and the QA runs are
invisible in /acts/<id>/runs (apify-publish skill), so a source outage that ends
on its own still leaves the warning up.

For every flagged actor this repo owns: run the prefill (10 rows, 256 MB). Rows
back -> PUT notice NONE and log HEALED. Otherwise log the run's status message,
which names the dead host (common/main.py). Costs ~$0.0006 per flagged actor per check.
Written 2026-11-16 when reddit-subreddit-posts was flagged through an Arctic Shift outage.
"""
import json
import pathlib
import subprocess
import sys
import time

import httpx

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from deploy import PROTECTED, default_input  # noqa: E402

API = "https://api.apify.com/v2"
T = subprocess.check_output(["security", "find-generic-password", "-s", "com.apify.cli", "-a", "token", "-w"], text=True).strip()
http = httpx.Client(headers={"Authorization": f"Bearer {T}"}, timeout=120)


def get(path, **kw):
    r = http.get(API + path, **kw)
    r.raise_for_status()
    return r.json()["data"]


def main():
    ours = {p.name for p in (ROOT / "actors").iterdir() if (p / "spec.json").exists()}
    flagged = []
    for a in get("/acts", params={"my": 1, "limit": 500})["items"]:
        if a["name"] in ours and a["name"] not in PROTECTED:
            full = get(f"/acts/{a['id']}")
            if full.get("notice") == "UNDER_MAINTENANCE":
                flagged.append(full)
    stamp = time.strftime("%F %T")
    if not flagged:
        print(f"{stamp} health: no actor under maintenance")
        return
    for act in flagged:
        spec = json.loads((ROOT / "actors" / act["name"] / "spec.json").read_text())
        inp = {**default_input(spec), "maxItems": 10}
        r = http.post(f"{API}/acts/{act['id']}/runs", params={"memory": 256}, json=inp)
        r.raise_for_status()
        run = r.json()["data"]
        while run["status"] in ("READY", "RUNNING"):
            run = get(f"/actor-runs/{run['id']}", params={"waitForFinish": 60})
        rows = len(http.get(f"{API}/datasets/{run['defaultDatasetId']}/items", params={"limit": 10}).json())
        if run["status"] == "SUCCEEDED" and rows:
            http.put(f"{API}/acts/{act['id']}", json={"notice": "NONE"}).raise_for_status()
            print(f"{stamp} HEALED {act['name']} ({rows} rows, run {run['id']})")
        else:
            print(f"{stamp} STILL DOWN {act['name']}: {run['status']} {rows} rows | {run.get('statusMessage')}")


if __name__ == "__main__":
    main()
