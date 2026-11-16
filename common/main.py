"""Actor entry point, shared by every actor in this repo (copied to src/__main__.py).

Each actor supplies src/impl.py with `async def run(inp, client, emit)`.
`emit(row)` pushes one dataset item; each item is one billable
`apify-default-dataset-item` event, so the platform charges per row and stops
the run when the user's max-charge budget is spent.
"""
import asyncio

import httpx
from apify import Actor

from .impl import run
from .lib import Client


class _Stop(Exception):
    pass


async def main() -> None:
    async with Actor:
        inp = await Actor.get_input() or {}
        max_items = int(inp.get("maxItems") or 0) or 10**9
        client = Client()
        count = 0
        buf: list[dict] = []

        async def flush():
            nonlocal buf
            if buf:
                res = await Actor.push_data(buf)
                buf = []
                if res is not None and getattr(res, "event_charge_limit_reached", False):
                    raise _Stop()

        async def emit(row: dict):
            nonlocal count
            if count >= max_items:
                raise _Stop()
            buf.append(row)
            count += 1
            if len(buf) >= 100:
                await flush()
            if count >= max_items:
                raise _Stop()

        upstream_down = None
        try:
            await run(inp, client, emit)
        except _Stop:
            pass
        except (httpx.HTTPStatusError, httpx.TransportError) as e:
            # The public source is down or refusing. Say so in plain words instead of a
            # traceback; rows already pushed are kept (and charged), nothing else is.
            try:
                host = e.request.url.host  # the property raises if httpx never set it
            except RuntimeError:
                host = "The source"
            code = f"HTTP {e.response.status_code}" if isinstance(e, httpx.HTTPStatusError) else type(e).__name__
            upstream_down = f"{host} is not responding ({code}). This is the public data source, not your input. {count} results returned; try again later."
        finally:
            try:
                await flush()
            except _Stop:
                pass
            await client.close()
        Actor.log.info(f"Done: {count} items")
        if upstream_down:
            Actor.log.error(upstream_down)
            await Actor.fail(status_message=upstream_down)
            return
        if count == 0:
            await Actor.set_status_message("No results matched this input.")
        else:
            await Actor.set_status_message(f"{count} results")


asyncio.run(main())
