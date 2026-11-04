FIELDS = ("NAME,CERT,FED_RSSD,CITY,STALP,ZIP,ADDRESS,ASSET,DEP,DEPDOM,NETINC,ROA,ROE,OFFICES,ESTYMD,ACTIVE,"
          "BKCLASS,REGAGNT,WEBADDR,HCTMULT,NAMEHCR,CHRTAGNT,INSDATE,REPDTE,LATITUDE,LONGITUDE,UNINUM")


async def run(inp, client, emit):
    f = []
    if inp.get("state"):
        f.append(f'STALP:{inp["state"].upper()}')
    if inp.get("activeOnly", True):
        f.append("ACTIVE:1")
    if inp.get("minAssetsThousands"):
        f.append(f'ASSET:[{int(inp["minAssetsThousands"])} TO *]')
    if inp.get("city"):
        f.append(f'CITY:"{inp["city"].upper()}"')
    params = {"fields": FIELDS, "sort_by": "ASSET", "sort_order": "DESC", "limit": 1000, "offset": 0, "format": "json"}
    if f:
        params["filters"] = " AND ".join(f)
    if inp.get("name"):
        params["search"] = f'NAME:{inp["name"]}'
    while True:
        d = await client.json("https://api.fdic.gov/banks/institutions", params=params)
        data = d.get("data", [])
        for x in data:
            r = x["data"]
            r["fdicUrl"] = f"https://banks.data.fdic.gov/bankfind-suite/bankfind/details/{r.get('CERT')}"
            await emit(r)
        params["offset"] += len(data)
        if not data or params["offset"] >= d.get("meta", {}).get("total", 0):
            return
