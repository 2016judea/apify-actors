"""Create/update an actor on Apify from actors/<name>/, build it, test-run it,
and (only if the test run returned rows) publish it to the Store with
pay-per-event pricing. Writes the result into ledger.tsv.

    .venv/bin/python scripts/deploy.py <name> [--no-publish] [--no-run]

Token: macOS Keychain, service com.apify.cli, account token.
"""
import json
import pathlib
import subprocess
import sys
import time

import httpx

ROOT = pathlib.Path(__file__).resolve().parent.parent
API = "https://api.apify.com/v2"
USER = "cheerful_term"
PROTECTED = {"breach-to-complaint"}  # another session's actor; never touch

TOKEN = subprocess.check_output(
    ["security", "find-generic-password", "-s", "com.apify.cli", "-a", "token", "-w"], text=True
).strip()
H = {"Authorization": f"Bearer {TOKEN}"}
http = httpx.Client(headers=H, timeout=httpx.Timeout(90, connect=20))

DOCKERFILE = """FROM apify/actor-python:3.12
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
CMD ["python3", "-m", "src"]
"""


def api(method, path, **kw):
    for i in range(5):
        r = http.request(method, API + path, **kw)
        if r.status_code in (429, 500, 502, 503) and i < 4:
            time.sleep(3 * (i + 1))
            continue
        if r.status_code >= 400:
            raise RuntimeError(f"{method} {path} -> {r.status_code} {r.text[:800]}")
        return r.json().get("data") if r.text else None


def input_schema(spec):
    props = {k: dict(v) for k, v in spec["input"]["properties"].items()}
    for k, v in props.items():
        v.setdefault("description", v.get("title", k))
    props.setdefault(
        "maxItems",
        {
            "title": "Max results",
            "type": "integer",
            "description": "Stop after this many results. Each result is billed as one event.",
            "editor": "number",
            "minimum": 1,
            "default": spec.get("defaultMax", 100),
            "prefill": spec.get("defaultMax", 100),
        },
    )
    return {
        "title": spec["title"],
        "type": "object",
        "schemaVersion": 1,
        "properties": props,
        "required": spec["input"].get("required", []),
    }


def output_schema(spec):
    # Store publication requires an output schema; it points the Output tab and the run's
    # `output` field at the default dataset, rendered through the "overview" view.
    return {
        "actorOutputSchemaVersion": 1,
        "title": f"{spec['title']}: output",
        "properties": {
            "overview": {
                "type": "string",
                "title": "Results",
                "template": "{{links.apiDefaultDatasetUrl}}/items?view=overview",
            }
        },
    }


def source_files(name, spec):
    d = ROOT / "actors" / name
    actor_json = {
        "actorSpecification": 1,
        "name": name,
        "title": spec["title"],
        "description": spec["description"],
        "version": "0.0",
        "buildTag": "latest",
        "input": "./input_schema.json",
        "output": "./output_schema.json",
        "dockerfile": "./Dockerfile",
        "readme": "../README.md",
        "storages": {
            "dataset": {
                "actorSpecification": 1,
                "views": {
                    "overview": {
                        "title": "Results",
                        "transformation": {"fields": spec.get("viewFields", [])} if spec.get("viewFields") else {},
                        "display": {"component": "table"},
                    }
                },
            }
        },
    }
    files = {
        ".actor/actor.json": json.dumps(actor_json, indent=2),
        ".actor/input_schema.json": json.dumps(input_schema(spec), indent=2),
        ".actor/output_schema.json": json.dumps(output_schema(spec), indent=2),
        "Dockerfile": DOCKERFILE,
        "requirements.txt": "apify>=2.7\nhttpx>=0.27\n" + "".join(x + "\n" for x in spec.get("requirements", [])),
        "README.md": (d / "README.md").read_text(),
        "src/__init__.py": "",
        "src/__main__.py": (ROOT / "common" / "main.py").read_text(),
        "src/lib.py": (ROOT / "common" / "lib.py").read_text(),
        "src/impl.py": (d / "impl.py").read_text(),
    }
    return [{"name": k, "format": "TEXT", "content": v} for k, v in files.items()]


def pricing(spec):
    events = {
        "apify-default-dataset-item": {
            "eventTitle": spec["eventTitle"],
            "eventDescription": spec["eventDescription"],
            "eventPriceUsd": spec["price"],
            "isPrimaryEvent": True,
        }
    }
    if spec.get("startPrice"):
        events["apify-actor-start"] = {
            "eventTitle": "Actor start",
            "eventDescription": "Charged once when the run starts (one event per GB of memory, minimum one).",
            "eventPriceUsd": spec["startPrice"],
            "isOneTimeEvent": True,
        }
    return [{"pricingModel": "PAY_PER_EVENT", "pricingPerEvent": {"actorChargeEvents": events}}]


def default_input(spec):
    out = {}
    for k, p in spec["input"]["properties"].items():
        if "prefill" in p:
            out[k] = p["prefill"]
        elif "default" in p:
            out[k] = p["default"]
    out.update(spec.get("testInput", {}))
    out["maxItems"] = spec.get("testMax", 10)
    return out


def ledger_update(name, **fields):
    import fcntl
    with open(ROOT / ".ledger.lock", "w") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        _ledger_update(name, **fields)


def _ledger_update(name, **fields):
    p = ROOT / "ledger.tsv"
    cols = ["actor", "source", "price_per_event_usd", "event", "competitor_prices", "test_run_rows", "store_url", "status"]
    rows = {}
    if p.exists():
        lines = p.read_text().splitlines()
        for ln in lines[1:]:
            parts = ln.split("\t")
            rows[parts[0]] = dict(zip(cols, parts + [""] * (len(cols) - len(parts))))
    r = rows.get(name, {c: "" for c in cols})
    r["actor"] = name
    r.update({k: str(v) for k, v in fields.items()})
    rows[name] = r
    out = ["\t".join(cols)] + ["\t".join(rows[k].get(c, "") for c in cols) for k in sorted(rows)]
    p.write_text("\n".join(out) + "\n")


def main():
    name = sys.argv[1]
    assert name not in PROTECTED
    no_publish = "--no-publish" in sys.argv
    no_run = "--no-run" in sys.argv
    spec = json.loads((ROOT / "actors" / name / "spec.json").read_text())
    assert len(spec["description"]) <= 300, "Apify caps description at 300 chars"
    body = {
        "name": name,
        "title": spec["title"],
        "description": spec["description"],
        "seoTitle": spec.get("seoTitle", spec["title"])[:60],
        "seoDescription": spec.get("seoDescription", spec["description"])[:160],
        "categories": spec["categories"],
        "defaultRunOptions": {"build": "latest", "timeoutSecs": 3600, "memoryMbytes": spec.get("memory", 256)},
        "exampleRunInput": {"body": json.dumps({**default_input(spec), "maxItems": spec.get("defaultMax", 100)}, indent=2),
                            "contentType": "application/json; charset=utf-8"},
        "versions": [
            {
                "versionNumber": "0.0",
                "sourceType": "SOURCE_FILES",
                "buildTag": "latest",
                "sourceFiles": source_files(name, spec),
            }
        ],
    }
    try:
        act = api("GET", f"/acts/{USER}~{name}")
    except RuntimeError:
        act = None
    if act:
        act = api("PUT", f"/acts/{act['id']}", json=body)
        print("updated", act["id"])
    else:
        act = api("POST", "/acts", json=body)
        print("created", act["id"])
    aid = act["id"]

    b = api("POST", f"/acts/{aid}/builds?version=0.0&tag=latest&useCache=true&waitForFinish=30")
    while b["status"] in ("READY", "RUNNING"):
        time.sleep(5)
        b = api("GET", f"/actor-builds/{b['id']}?waitForFinish=30")
    print("build", b["status"])
    if b["status"] != "SUCCEEDED":
        log = http.get(f"{API}/logs/{b['id']}").text
        print(log[-3000:])
        ledger_update(name, source=spec.get("source", ""), status="build-failed")
        sys.exit(1)
    if no_run:
        return

    inp = default_input(spec)
    run = api("POST", f"/acts/{aid}/runs?memory={spec.get('memory', 256)}&waitForFinish=30", json=inp)
    while run["status"] in ("READY", "RUNNING"):
        time.sleep(5)
        run = api("GET", f"/actor-runs/{run['id']}?waitForFinish=30")
    # dataset itemCount lags a few seconds behind the run; count the items themselves
    rows = 0
    for _ in range(6):
        items = http.get(f"{API}/datasets/{run['defaultDatasetId']}/items?limit=1000").json()
        rows = len(items)
        if rows:
            break
        time.sleep(3)
    print("run", run["status"], "rows", rows, "run", run["id"])
    if run["status"] != "SUCCEEDED" or rows == 0:
        print(http.get(f"{API}/logs/{run['id']}").text[-3000:])
        ledger_update(name, source=spec.get("source", ""), test_run_rows=rows, status=f"test-{run['status'].lower()}-{rows}rows")
        sys.exit(1)
    sample = http.get(f"{API}/datasets/{run['defaultDatasetId']}/items?limit=1").json()
    print("sample", json.dumps(sample, default=str)[:600])

    url = f"https://apify.com/{USER}/{name}"
    status = "tested-private"
    if not no_publish:
        try:
            cur = api("GET", f"/acts/{aid}").get("pricingInfos") or []
            want = pricing(spec)[0]["pricingPerEvent"]["actorChargeEvents"]
            have = cur[-1]["pricingPerEvent"]["actorChargeEvents"] if cur else None
            # Apify rejects pricing edits that are too frequent; only PUT when it differs.
            if have != want:
                api("PUT", f"/acts/{aid}", json={"pricingInfos": pricing(spec)})
            status = "priced"
        except RuntimeError as e:
            print("PRICING FAILED", e)
            status = "pricing-blocked"
        try:
            api("PUT", f"/acts/{aid}", json={"isPublic": True})
            status = "public-" + status
        except RuntimeError as e:
            print("PUBLISH FAILED", str(e)[:300])
            status += "-awaiting-store-terms" if "store-terms-not-accepted" in str(e) else "-publish-blocked"
    ledger_update(
        name,
        source=spec.get("source", ""),
        price_per_event_usd=spec["price"],
        event=spec["eventTitle"],
        competitor_prices=spec.get("competitors", ""),
        test_run_rows=rows,
        store_url=url,
        status=status,
    )
    print("STATUS", status, url)


if __name__ == "__main__":
    main()
