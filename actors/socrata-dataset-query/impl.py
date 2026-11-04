from .lib import socrata_query


async def run(inp, client, emit):
    async for r in socrata_query(client, inp.get("domain") or "data.cityofchicago.org", inp.get("datasetId") or "ydr8-5enu",
                                 where=inp.get("where") or None, order=inp.get("order") or None, q=inp.get("q") or None,
                                 select=inp.get("select") or None, limit=int(inp.get("maxItems") or 1000)):
        await emit(r)
