async def run(inp, client, emit):
    for a in [x for x in (inp.get("addresses") or []) if x.strip()]:
        d = await client.json("https://geocoding.geo.census.gov/geocoder/geographies/onelineaddress",
                              params={"address": a, "benchmark": "Public_AR_Current", "vintage": "Current_Current", "format": "json"})
        m = (d.get("result", {}).get("addressMatches") or [None])[0]
        if not m:
            await emit({"input": a, "matched": False})
            continue
        g = m.get("geographies", {})
        def first(k):
            return (g.get(k) or [{}])[0]
        tract, county, state = first("Census Tracts"), first("Counties"), first("States")
        bg = first("Census Block Groups") or first("2020 Census Blocks")
        place = first("Incorporated Places")
        cd = next((v[0] for k, v in g.items() if "Congressional" in k and v), {})
        await emit({
            "input": a, "matched": True, "matchedAddress": m.get("matchedAddress"),
            "longitude": m["coordinates"]["x"], "latitude": m["coordinates"]["y"],
            "stateFips": state.get("STATE"), "state": state.get("STUSAB"), "countyFips": county.get("GEOID"), "county": county.get("NAME"),
            "tractGeoid": tract.get("GEOID"), "tract": tract.get("NAME"), "blockGroupGeoid": bg.get("GEOID"),
            "place": place.get("NAME"), "placeGeoid": place.get("GEOID"),
            "congressionalDistrict": cd.get("NAME"), "tigerLineId": (m.get("tigerLine") or {}).get("tigerLineId"),
        })
