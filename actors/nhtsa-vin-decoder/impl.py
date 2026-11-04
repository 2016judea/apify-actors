from .lib import compact


async def run(inp, client, emit):
    vins = [v.strip().upper() for v in (inp.get("vins") or []) if v.strip()]
    for i in range(0, len(vins), 50):
        chunk = vins[i:i + 50]
        r = await client.post("https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/",
                              data={"format": "json", "DATA": ";".join(chunk)})
        for row in r.json().get("Results", []):
            row = compact({k: (v.strip() if isinstance(v, str) else v) for k, v in row.items()})
            await emit(row)
