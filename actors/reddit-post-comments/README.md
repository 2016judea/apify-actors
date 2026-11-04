# Reddit Post Comments (Full Thread)

Every comment on one or more Reddit posts, with nesting depth, parent, author, score and time, from the Arctic Shift archive. Pass post URLs or IDs.

## Who it's for

- Reading the whole discussion under a launch, complaint or AMA
- Sentiment and voice-of-customer analysis
- Training and evaluation datasets

## Input

| Field | What it does |
|---|---|
| `posts` | **Post URLs or IDs**. e.g. https://www.reddit.com/r/smallbusiness/comments/abc123/... or abc123 |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "posts": [
    "1xeo2j5"
  ],
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "postId": "1xeo2j5",
  "commentId": "19rlv9kbyvobo",
  "parentId": "t3_1xeo2j5",
  "depth": 0,
  "author": "AutoModerator",
  "body": "**Friendly Reminder**\n\nr/smallbusiness is a question and answer subreddit. Ask a question about starting, owning, and growing a small business and the community answers. Posts that violate the rules listed in the sidebar will be removed. \n\n**Please do not conduct market research on our community.**\n\nWe are not your focus group and asking us about our pain points, needs, what is hardest about X, etc. is not asking about how small business works or for real help with running your small business. \n\nThese posts are subject to removal and given the community's disgust with the constant spamming of these posts you might just destroy your brand and contaminate your company search results. \n\nSeeing this message does not mean your post was automatically removed. If you asked about pain points or are directly or indirectly promoting a product please remove your post. Come back to post an honest question or give a knowledgeable response to someone else's question and leave your company name in your own profile. We can tell if you know what you're doing and the community can reach out if they need to.\n\n**We welcome honest question posts, especially from newcomers.** \nThank you for your post.\n\n*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](/message/compose/?to=/r/smallbusiness) if you have any questions or concerns.*",
  "score": 1,
  "createdAt": "2026-10-25T00:18:56Z",
  "url": "https://www.reddit.com/comments/1xeo2j5/_/19rlv9kbyvobo"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per comment** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://arctic-shift.photon-reddit.com/api/comments/tree

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~reddit-post-comments/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"posts": ["1xeo2j5"], "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
