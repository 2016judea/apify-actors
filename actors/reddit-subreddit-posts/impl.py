import datetime as dt

API = "https://arctic-shift.photon-reddit.com/api/posts/search"


async def run(inp, client, emit):
    sub = (inp.get("subreddit") or "smallbusiness").removeprefix("r/")
    after = inp.get("after") or (dt.date.today() - dt.timedelta(days=7)).isoformat()
    before = inp.get("before")
    kws = [k.strip().lower() for k in (inp.get("keywords") or []) if k.strip()]
    min_score = int(inp.get("minScore") or 0)
    seen = set()
    cur = after
    while True:
        params = {"subreddit": sub, "after": cur, "limit": 100, "sort": "asc"}
        if before:
            params["before"] = before
        d = await client.json(API, params=params)
        posts = d.get("data") or []
        new = 0
        for p in posts:
            if p["id"] in seen:
                continue
            seen.add(p["id"])
            new += 1
            text = (p.get("title", "") + " " + (p.get("selftext") or "")).lower()
            if kws and not any(k in text for k in kws):
                continue
            if (p.get("score") or 0) < min_score:
                continue
            await emit({
                "id": p["id"], "subreddit": p.get("subreddit"), "title": p.get("title"), "text": p.get("selftext"),
                "author": p.get("author"), "score": p.get("score"), "numComments": p.get("num_comments"),
                "flair": p.get("link_flair_text"),
                "createdAt": dt.datetime.fromtimestamp(p["created_utc"], dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "url": "https://www.reddit.com" + p.get("permalink", ""), "link": p.get("url"),
            })
        if len(posts) < 100 or not new:
            return
        # `after` is exclusive and second-granular: restart one second before the newest seen, de-dupe by id
        last = max(p["created_utc"] for p in posts) - 1
        cur = dt.datetime.fromtimestamp(last, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
