"""Generate actors/<name>/README.md from spec.json + sample.json.

    .venv/bin/python scripts/readme.py <name>
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent


def build(name):
    d = ROOT / "actors" / name
    spec = json.loads((d / "spec.json").read_text())
    sample = json.loads((d / "sample.json").read_text()) if (d / "sample.json").exists() else None
    props = spec["input"]["properties"]
    lines = [f"# {spec['title']}", "", spec["description"], ""]
    if spec.get("why"):
        lines += ["## Why use it", "", spec["why"], ""]
    if spec.get("useCases"):
        lines += ["## Who it's for", ""] + [f"- {u}" for u in spec["useCases"]] + [""]
    lines += ["## Input", "", "| Field | What it does |", "|---|---|"]
    for k, p in props.items():
        desc = p.get("description", "").replace("|", "/")
        lines.append(f"| `{k}` | **{p.get('title', k)}**. {desc} |")
    lines.append("| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |")
    ex = {k: (p.get("prefill", p.get("default"))) for k, p in props.items() if "prefill" in p or "default" in p}
    ex.update(spec.get("testInput", {}))
    ex["maxItems"] = spec.get("defaultMax", 100)
    lines += ["", "Example input:", "", "```json", json.dumps(ex, indent=2), "```", ""]
    if sample:
        lines += ["## Output", "", "One dataset item per result. A real item from a test run:", "", "```json",
                  json.dumps(sample, indent=2, default=str)[:2500], "```", "",
                  "Download as JSON, CSV, Excel or via the Apify API.", ""]
    lines += ["## Pricing", "",
              f"Pay per result: **${spec['price']} per {spec['eventTitle'].lower()}** "
              f"(${spec['price'] * 1000:g} per 1,000). No monthly fee. Set a max charge on the run and it stops there. "
              "AI agents can run it with agentic payments where Apify enables them.", ""]
    lines += ["## Data source", "", spec.get("sourceNote", f"Fetched live at run time from the public source: {spec.get('source','')}"),
              "", "Public records only. Nothing is fetched behind a login.", ""]
    if spec.get("limits"):
        lines += ["## Limits", ""] + [f"- {x}" for x in spec["limits"]] + [""]
    lines += ["## Use it from code or an AI agent", "", "```bash",
              f"curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~{name}/run-sync-get-dataset-items?token=YOUR_TOKEN' \\",
              "  -H 'Content-Type: application/json' -d '" + json.dumps(ex) + "'", "```", "",
              "Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term", ""]
    (d / "README.md").write_text("\n".join(lines))


if __name__ == "__main__":
    for n in sys.argv[1:]:
        build(n)
