"""Tiny helpers for writing actor spec.json/config.json from Python one-offs."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent

def s(title, desc, prefill=None, **kw):
    p = {"title": title, "type": "string", "editor": "textfield", "description": desc, **kw}
    if prefill is not None: p["prefill"] = prefill
    return p

def n(title, desc, prefill=None, **kw):
    p = {"title": title, "type": "integer", "editor": "number", "description": desc, **kw}
    if prefill is not None: p["prefill"] = prefill
    return p

def e(title, desc, options, prefill=None):
    p = {"title": title, "type": "string", "editor": "select", "description": desc, "enum": options}
    if prefill is not None: p["prefill"] = prefill; p["default"] = prefill
    return p

def b(title, desc, default=False):
    return {"title": title, "type": "boolean", "editor": "checkbox", "description": desc, "default": default}

def write(name, spec, config=None):
    d = ROOT / "actors" / name
    d.mkdir(parents=True, exist_ok=True)
    (d / "spec.json").write_text(json.dumps(spec, indent=2) + "\n")
    if config is not None:
        (d / "config.json").write_text(json.dumps(config, indent=2) + "\n")
