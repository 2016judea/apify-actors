from .lib import arcgis_query, iso_dates, sql_quote

LAYER = "https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/CCS_Permits/FeatureServer/0"


async def run(inp, client, emit):
    where = ["1=1"]
    if inp.get("issuedSince"):
        where.append(f"issueDate >= DATE {sql_quote(inp['issuedSince'])}")
    if inp.get("permitType"):
        where.append(f"permitType = {sql_quote(inp['permitType'])}")
    if inp.get("workType"):
        where.append(f"UPPER(workType) LIKE {sql_quote('%' + inp['workType'].upper() + '%')}")
    if inp.get("minValue"):
        where.append(f"permit_Value >= {float(inp['minValue'])}")
    if inp.get("neighborhood"):
        where.append(f"UPPER(Neighborhoods_Desc) = {sql_quote(inp['neighborhood'].upper())}")
    if inp.get("keyword"):
        where.append(f"UPPER(comments) LIKE {sql_quote('%' + inp['keyword'].upper() + '%')}")
    async for r in arcgis_query(client, LAYER, where=" AND ".join(where), order_by="issueDate DESC",
                                limit=int(inp.get("maxItems") or 100)):
        r.pop("OBJECTID", None)
        r = iso_dates(r, ["issueDate", "completeDate"])
        r["address"] = r.pop("Display", None)
        r["ownerName"] = r.pop("fullName", None)
        r["source"] = "City of Minneapolis CCS_Permits (opendata.minneapolismn.gov)"
        await emit(r)
