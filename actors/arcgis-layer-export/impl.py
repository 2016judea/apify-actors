from .lib import arcgis_query, iso_dates


async def run(inp, client, emit):
    layer = inp.get("layerUrl") or "https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/CCS_Permits/FeatureServer/0"
    layer = layer.split("/query")[0].rstrip("/")
    meta = await client.json(layer, params={"f": "json"})
    if "error" in meta:
        raise RuntimeError(f"Not a readable ArcGIS layer: {meta['error']}")
    page = min(int(meta.get("maxRecordCount") or 1000), 2000)
    async for r in arcgis_query(client, layer, where=inp.get("where") or "1=1", out_fields=inp.get("outFields") or "*",
                                order_by=inp.get("orderBy") or None, limit=int(inp.get("maxItems") or 1000),
                                page_size=page, geometry=bool(inp.get("includeGeometry"))):
        await emit(iso_dates(r))
