import datetime as dt
import re


def walk(nodes, depth=0):
    for n in nodes or []:
        d = n.get("data", n)
        if n.get("kind") == "more" or "body" not in d:
            continue
        yield d, depth
        rep = d.get("replies")
        if isinstance(rep, dict):
            yield from walk(rep.get("data", {}).get("children"), depth + 1)
        elif isinstance(rep, list):
            yield from walk(rep, depth + 1)


async def run(inp, client, emit):
    for u in [x for x in (inp.get("posts") or []) if x.strip()]:
        m = re.search(r"comments/([a-z0-9]+)", u)
        pid = m.group(1) if m else u.strip().removeprefix("t3_")
        d = await client.json("https://arctic-shift.photon-reddit.com/api/comments/tree",
                              params={"link_id": f"t3_{pid}", "limit": 9999})
        for c, depth in walk(d.get("data")):
            await emit({
                "postId": pid, "commentId": c.get("id"), "parentId": c.get("parent_id"), "depth": depth,
                "author": c.get("author"), "body": c.get("body"), "score": c.get("score"),
                "createdAt": dt.datetime.fromtimestamp(c["created_utc"], dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") if c.get("created_utc") else None,
                "url": f"https://www.reddit.com/comments/{pid}/_/{c.get('id')}",
            })
