# Reddit Subreddit Posts by Date & Keyword

Every post in a subreddit for a date window, from the Arctic Shift Reddit archive (no login, no Reddit API): title, text, author, score, comments, flair, time and permalink. Filter locally by keywords and minimum score. Pages oldest-first so nothing is dropped.

## Why use it

Archive search APIs silently cap a request at ~100 rows and drop the rest of the window. This actor pages oldest-first with a moving cursor, so a busy day of a big subreddit comes back whole.

## Who it's for

- Founders and marketers mining what customers actually say (pain points, tools, prices)
- Brand and competitor monitoring
- Researchers building datasets

## Input

| Field | What it does |
|---|---|
| `subreddit` | **Subreddit**. Without r/ |
| `after` | **From date (YYYY-MM-DD)**. Start of the window. |
| `before` | **To date (YYYY-MM-DD)**. End of the window (default: now). |
| `keywords` | **Keywords (any)**. Keep posts whose title or text contains any of these. Empty keeps all. |
| `minScore` | **Minimum score**. Keep posts at or above this score. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "subreddit": "smallbusiness",
  "after": "2026-10-25",
  "keywords": [
    "pricing"
  ],
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "id": "1xeub8s",
  "subreddit": "smallbusiness",
  "title": "Asking for a discount",
  "text": "I recently got a call from someone asking for pricing on a washer and dryer.  I gave a price, what I felt as fair. Then the woman say I am a restaurant down the street from you, can you give a neighbor discount. I said I have given pretty good prices. She says they are pretty much the same as everybody else.  I say let me get back to you. So I do a little better on the price and say 99.00 for delivery and install. I send an estimate to them. I hear nothing. They said they wanted them by the week of the 23.  So I text the girlfriend, what day do you want these installed. She says we are we are waiting on the floor and painting to be done. I say ok. Let me know when you are ready.  Then I get a call from her boyfriend. He came to my store and spoke to me about pricing and such. I told him I was charging for install. He asks if I want a deposit, I say no just pay when we deliver them. <\u2014 back story. He says I told you we want these, and you didn\u2019t want payment. I got your message estimate and you  charged an extra 100.00 we didn\u2019t talk about.   \nAt this point. I may tell them I do not want to do business with them. I would never go to their restaurant and ask for a discount. I think it was rude and tacky. Then the whole experience with me asking if they were ready for the delivery. I am a small mom and pop. I don\u2019t have the washer and dryer they want  in stock.   \nI will keep you posted. I may decline this transaction. They just seem wrong to me. ",
  "author": "Worldly-Relief2732",
  "score": 32,
  "numComments": 29,
  "flair": null,
  "createdAt": "2026-10-25T05:49:37Z",
  "url": "https://www.reddit.com/r/smallbusiness/comments/1xeub8s/asking_for_a_discount/",
  "link": "https://www.reddit.com/r/smallbusiness/comments/1xeub8s/asking_for_a_discount/"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.008 per post** ($8 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://arctic-shift.photon-reddit.com/api/posts/search

Public records only. Nothing is fetched behind a login.

## Limits

- Data comes from the Arctic Shift archive, typically a day or two behind Reddit.
- Deleted and removed posts appear as the archive captured them.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~reddit-subreddit-posts/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"subreddit": "smallbusiness", "after": "2026-10-25", "keywords": ["pricing"], "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
