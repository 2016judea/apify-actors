"""Shared helpers for every actor in this repo.

Copied into each actor's src/ at deploy time by scripts/deploy.py, so edit it
here, never in an actor directory.
"""
from __future__ import annotations

import asyncio
import json
from typing import Any, AsyncIterator

import httpx

UA = "apify-actors/1.0 (public-records actor; contact aidan@brickandmortar.dev)"


class Client:
    def __init__(self, headers: dict | None = None, timeout: float = 60.0):
        h = {"User-Agent": UA, "Accept": "application/json"}
        h.update(headers or {})
        self.c = httpx.AsyncClient(headers=h, timeout=timeout, follow_redirects=True)

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
