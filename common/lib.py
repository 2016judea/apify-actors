"""Shared helpers for every actor in this repo.

Copied into each actor's src/ at deploy time by scripts/deploy.py, so edit it
here, never in an actor directory.
"""
from __future__ import annotations

import asyncio
import json
from typing import Any, AsyncIterator

import ssl

import certifi
import httpx

# Intermediates that some government servers fail to send. Browsers and macOS
# curl fetch a missing intermediate via AIA; Python's ssl does not, so the run
# dies with CERTIFICATE_VERIFY_FAILED. oig.hhs.gov (LEIE) has served a Sectigo
# DV R36 leaf with an unrelated SSL.com chain since ~2026-11-04, which failed
# Apify's daily QA three days running. Fetched from the leaf's AIA URL
# (http://crt.sectigo.com/SectigoPublicServerAuthenticationCADVR36.crt); it
# chains to Sectigo Root R46, which certifi already trusts. Expires 2036-03-21.
EXTRA_INTERMEDIATES = """
-----BEGIN CERTIFICATE-----
MIIGTDCCBDSgAwIBAgIQOXpmzCdWNi4NqofKbqvjsTANBgkqhkiG9w0BAQwFADBf
MQswCQYDVQQGEwJHQjEYMBYGA1UEChMPU2VjdGlnbyBMaW1pdGVkMTYwNAYDVQQD
Ey1TZWN0aWdvIFB1YmxpYyBTZXJ2ZXIgQXV0aGVudGljYXRpb24gUm9vdCBSNDYw
HhcNMjEwMzIyMDAwMDAwWhcNMzYwMzIxMjM1OTU5WjBgMQswCQYDVQQGEwJHQjEY
MBYGA1UEChMPU2VjdGlnbyBMaW1pdGVkMTcwNQYDVQQDEy5TZWN0aWdvIFB1Ymxp
YyBTZXJ2ZXIgQXV0aGVudGljYXRpb24gQ0EgRFYgUjM2MIIBojANBgkqhkiG9w0B
AQEFAAOCAY8AMIIBigKCAYEAljZf2HIz7+SPUPQCQObZYcrxLTHYdf1ZtMRe7Yeq
RPSwygz16qJ9cAWtWNTcuICc++p8Dct7zNGxCpqmEtqifO7NvuB5dEVexXn9RFFH
12Hm+NtPRQgXIFjx6MSJcNWuVO3XGE57L1mHlcQYj+g4hny90aFh2SCZCDEVkAja
EMMfYPKuCjHuuF+bzHFb/9gV8P9+ekcHENF2nR1efGWSKwnfG5RawlkaQDpRtZTm
M64TIsv/r7cyFO4nSjs1jLdXYdz5q3a4L0NoabZfbdxVb+CUEHfB0bpulZQtH1Rv
38e/lIdP7OTTIlZh6OYL6NhxP8So0/sht/4J9mqIGxRFc0/pC8suja+wcIUna0HB
pXKfXTKpzgis+zmXDL06ASJf5E4A2/m+Hp6b84sfPAwQ766rI65mh50S0Di9E3Pn
2WcaJc+PILsBmYpgtmgWTR9eV9otfKRUBfzHUHcVgarub/XluEpRlTtZudU5xbFN
xx/DgMrXLUAPaI60fZ6wA+PTAgMBAAGjggGBMIIBfTAfBgNVHSMEGDAWgBRWc1hk
lfmSGrASKgRieaFAFYghSTAdBgNVHQ4EFgQUaMASFhgOr872h6YyV6NGUV3LBycw
DgYDVR0PAQH/BAQDAgGGMBIGA1UdEwEB/wQIMAYBAf8CAQAwHQYDVR0lBBYwFAYI
KwYBBQUHAwEGCCsGAQUFBwMCMBsGA1UdIAQUMBIwBgYEVR0gADAIBgZngQwBAgEw
VAYDVR0fBE0wSzBJoEegRYZDaHR0cDovL2NybC5zZWN0aWdvLmNvbS9TZWN0aWdv
UHVibGljU2VydmVyQXV0aGVudGljYXRpb25Sb290UjQ2LmNybDCBhAYIKwYBBQUH
AQEEeDB2ME8GCCsGAQUFBzAChkNodHRwOi8vY3J0LnNlY3RpZ28uY29tL1NlY3Rp
Z29QdWJsaWNTZXJ2ZXJBdXRoZW50aWNhdGlvblJvb3RSNDYucDdjMCMGCCsGAQUF
BzABhhdodHRwOi8vb2NzcC5zZWN0aWdvLmNvbTANBgkqhkiG9w0BAQwFAAOCAgEA
YtOC9Fy+TqECFw40IospI92kLGgoSZGPOSQXMBqmsGWZUQ7rux7cj1du6d9rD6C8
ze1B2eQjkrGkIL/OF1s7vSmgYVafsRoZd/IHUrkoQvX8FZwUsmPu7amgBfaY3g+d
q1x0jNGKb6I6Bzdl6LgMD9qxp+3i7GQOnd9J8LFSietY6Z4jUBzVoOoz8iAU84OF
h2HhAuiPw1ai0VnY38RTI+8kepGWVfGxfBWzwH9uIjeooIeaosVFvE8cmYUB4TSH
5dUyD0jHct2+8ceKEtIoFU/FfHq/mDaVnvcDCZXtIgitdMFQdMZaVehmObyhRdDD
4NQCs0gaI9AAgFj4L9QtkARzhQLNyRf87Kln+YU0lgCGr9HLg3rGO8q+Y4ppLsOd
unQZ6ZxPNGIfOApbPVf5hCe58EZwiWdHIMn9lPP6+F404y8NNugbQixBber+x536
WrZhFZLjEkhp7fFXf9r32rNPfb74X/U90Bdy4lzp3+X1ukh1BuMxA/EEhDoTOS3l
7ABvc7BYSQubQ2490OcdkIzUh3ZwDrakMVrbaTxUM2p24N6dB+ns2zptWCva6jzW
r8IWKIMxzxLPv5Kt3ePKcUdvkBU/smqujSczTzzSjIoR5QqQA6lN1ZRSnuHIWCvh
JEltkYnTAH41QJ6SAWO66GrrUESwN/cgZzL4JLEqz1Y=
-----END CERTIFICATE-----
"""


def ssl_context() -> ssl.SSLContext:
    ctx = ssl.create_default_context(cafile=certifi.where())
    ctx.load_verify_locations(cadata=EXTRA_INTERMEDIATES)
    return ctx


UA = "apify-actors/1.0 (public-records actor; contact aidan@brickandmortar.dev)"


class Client:
    def __init__(self, headers: dict | None = None, timeout: float = 60.0):
        h = {"User-Agent": UA, "Accept": "application/json"}
        h.update(headers or {})
        self.c = httpx.AsyncClient(headers=h, timeout=timeout, follow_redirects=True, verify=ssl_context())

    async def get(self, url: str, params: dict | None = None, **kw) -> httpx.Response:
        return await self._req("GET", url, params=params, **kw)

    async def post(self, url: str, **kw) -> httpx.Response:
        return await self._req("POST", url, **kw)

    async def _req(self, method: str, url: str, **kw) -> httpx.Response:
        delay = 2.0
        for attempt in range(6):
            try:
                r = await self.c.request(method, url, **kw)
            except (httpx.TransportError, httpx.TimeoutException):
                if attempt == 5:
                    raise
                await asyncio.sleep(delay)
                delay *= 2
                continue
            if r.status_code in (429, 500, 502, 503, 504) and attempt < 5:
                ra = r.headers.get("retry-after")
                await asyncio.sleep(float(ra) if ra and ra.isdigit() else delay)
                delay *= 2
                continue
            r.raise_for_status()
            return r
        raise RuntimeError("unreachable")

    async def json(self, url: str, params: dict | None = None, **kw) -> Any:
        r = await self.get(url, params=params, **kw)
        return r.json()

    async def close(self):
        await self.c.aclose()


async def arcgis_query(
    client: Client,
    layer_url: str,
    where: str = "1=1",
    out_fields: str = "*",
    order_by: str | None = None,
    limit: int = 1000,
    page_size: int = 1000,
    geometry: bool = False,
    extra: dict | None = None,
) -> AsyncIterator[dict]:
    """Page through an ArcGIS FeatureServer/MapServer layer.

    ArcGIS caps each read at the layer's maxRecordCount (often 1,000 or 2,000)
    and says so only through `exceededTransferLimit`, so we page with
    resultOffset until fewer rows come back or the limit is met.
    """
    offset = 0
    got = 0
    while got < limit:
        n = min(page_size, limit - got)
        params = {
            "where": where,
            "outFields": out_fields,
            "returnGeometry": "true" if geometry else "false",
            "outSR": "4326",
            "resultOffset": offset,
            "resultRecordCount": n,
            "f": "json",
        }
        if order_by:
            params["orderByFields"] = order_by
        if extra:
            params.update(extra)
        d = await client.json(layer_url.rstrip("/") + "/query", params=params)
        if "error" in d:
            raise RuntimeError(f"ArcGIS error: {d['error']}")
        feats = d.get("features", [])
        if not feats:
            return
        for f in feats:
            row = dict(f.get("attributes") or {})
            g = f.get("geometry")
            if geometry and g:
                if "x" in g:
                    row["longitude"], row["latitude"] = g.get("x"), g.get("y")
                else:
                    row["geometry"] = g
            yield row
            got += 1
            if got >= limit:
                return
        offset += len(feats)
        if len(feats) < n and not d.get("exceededTransferLimit"):
            return


def epoch_ms_to_iso(v):
    """ArcGIS dates are epoch milliseconds; return ISO date strings."""
    import datetime as dt

    if isinstance(v, (int, float)) and v > 10_000_000_000 or isinstance(v, (int, float)) and v < -10_000_000_000:
        try:
            return dt.datetime.fromtimestamp(v / 1000, tz=dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        except (OverflowError, OSError, ValueError):
            return v
    return v


def iso_dates(row: dict, keys: list[str] | None = None) -> dict:
    for k, v in list(row.items()):
        if keys is None or k in keys:
            if isinstance(v, (int, float)) and (keys is not None or "date" in k.lower() or k.lower().endswith("_dt")):
                row[k] = epoch_ms_to_iso(v)
    return row


async def socrata_query(
    client: Client,
    domain: str,
    dataset: str,
    where: str | None = None,
    order: str | None = None,
    limit: int = 1000,
    select: str | None = None,
    q: str | None = None,
) -> AsyncIterator[dict]:
    offset = 0
    got = 0
    while got < limit:
        n = min(1000, limit - got)
        params = {"$limit": n, "$offset": offset}
        if where:
            params["$where"] = where
        if order:
            params["$order"] = order
        if select:
            params["$select"] = select
        if q:
            params["$q"] = q
        rows = await client.json(f"https://{domain}/resource/{dataset}.json", params=params)
        if not rows:
            return
        for r in rows:
            yield r
            got += 1
            if got >= limit:
                return
        offset += len(rows)
        if len(rows) < n:
            return


def sql_quote(s: str) -> str:
    return "'" + str(s).replace("'", "''") + "'"


def compact(d: dict) -> dict:
    return {k: v for k, v in d.items() if v not in (None, "", [], {})}


def dumps(x) -> str:
    return json.dumps(x, default=str)


def _clause(op: str, field: str, v) -> str | None:
    if v is None or v == "" or v == []:
        return None
    if op == "eq":
        return f"{field} = {sql_quote(v)}" if isinstance(v, str) else f"{field} = {v}"
    if op == "ieq":
        return f"UPPER({field}) = {sql_quote(str(v).upper())}"
    if op == "like":
        return f"UPPER({field}) LIKE {sql_quote('%' + str(v).upper() + '%')}"
    if op == "prefix":
        return f"UPPER({field}) LIKE {sql_quote(str(v).upper() + '%')}"
    if op == "gte":
        return f"{field} >= {float(v)}"
    if op == "lte":
        return f"{field} <= {float(v)}"
    if op == "date_gte":
        return f"{field} >= DATE {sql_quote(v)}"
    if op == "date_lte":
        return f"{field} <= DATE {sql_quote(v)}"
    if op == "in":
        vals = v if isinstance(v, list) else [x.strip() for x in str(v).split(",") if x.strip()]
        return f"{field} IN ({','.join(sql_quote(x) for x in vals)})"
    if op == "sgte":
        return f"{field} >= {sql_quote(v)}"
    if op == "slte":
        return f"{field} <= {sql_quote(v)}"
    if op == "bool":
        return field if v else None
    raise ValueError(op)


async def arcgis_actor(cfg: dict, inp: dict, client: Client, emit) -> None:
    """Config-driven ArcGIS actor: filters map input keys to SQL clauses."""
    layer = cfg["layer"]
    if "layerByInput" in cfg:
        key, table = cfg["layerByInput"]
        layer = table[inp.get(key) or next(iter(table))]
    where = [cfg.get("baseWhere", "1=1")]
    for f in cfg.get("filters", []):
        c = _clause(f["op"], f["field"], inp.get(f["input"]))
        if c:
            where.append(c)
    drop = set(cfg.get("drop", []))
    rename = cfg.get("rename", {})
    dates = cfg.get("dates")
    async for r in arcgis_query(client, layer, where=" AND ".join(where), order_by=cfg.get("order"), out_fields=cfg.get("outFields", "*"),
                                limit=int(inp.get("maxItems") or 100), geometry=cfg.get("geometry", False),
                                page_size=cfg.get("pageSize", 1000)):
        for k in drop:
            r.pop(k, None)
        r = iso_dates(r, dates)
        out = {rename.get(k, k): (v.strip() if isinstance(v, str) else v) for k, v in r.items()}
        out.update(cfg.get("static", {}))
        await emit(out)
