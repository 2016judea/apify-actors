"""Run an actor's impl locally (no Apify compute) and print what it emits.

    .venv/bin/python scripts/local.py <actor-dir-name> [json-input-overrides]
"""
import asyncio
import importlib.util
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "common"))
import lib  # noqa: E402


def default_input(spec: dict) -> dict:
    out = {}
    for k, p in spec["input"]["properties"].items():
        if "prefill" in p:
            out[k] = p["prefill"]
        elif "default" in p:
            out[k] = p["default"]
    out.update(spec.get("testInput", {}))
    return out


async def main():
    name = sys.argv[1]
    d = ROOT / "actors" / name
    spec = json.loads((d / "spec.json").read_text())
    inp = default_input(spec)
    if len(sys.argv) > 2 and sys.argv[2].startswith("{"):
        inp.update(json.loads(sys.argv[2]))
    inp.setdefault("maxItems", 5)
    src = (d / "impl.py").read_text().replace("from .lib import", "from lib import")
    mod = type(sys)("impl")
    exec(compile(src, str(d / "impl.py"), "exec"), mod.__dict__)
    rows = []

    class Stop(Exception):
        pass

    async def emit(r):
        rows.append(r)
        if len(rows) >= inp["maxItems"]:
            raise Stop()

    c = lib.Client()
    try:
        await mod.run(inp, c, emit)
    except Stop:
        pass
    finally:
        await c.close()
    print(json.dumps(rows[:3], indent=1, default=str)[:3000])
    if rows and "--save" in sys.argv:
        (d / "sample.json").write_text(json.dumps(rows[0], indent=2, default=str) + "\n")
    print(f"ROWS={len(rows)} input={json.dumps(inp)}")


asyncio.run(main())
