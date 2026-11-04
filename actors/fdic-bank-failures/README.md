# FDIC Failed Banks

Every US bank failure the FDIC has recorded since 1934: bank name, cert, city and state, failure date, resolution type, acquirer path, assets and deposits at failure, and estimated cost to the Deposit Insurance Fund.

## Who it's for

- Credit and banking analysts studying failure history
- Journalists
- Risk models needing a labeled failure set

## Input

| Field | What it does |
|---|---|
| `state` | **State**. Two-letter code, e.g. CA |
| `failedSince` | **Failed on or after (YYYY-MM-DD)**. Only failures on or after this date. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "failedSince": "2008-01-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "QBFDEP": 68773,
  "PSTALP": "KS",
  "FIN": "10553",
  "FAILDATE": "7/17/2026",
  "CITYST": "LENEXA, KS",
  "RESTYPE": "FAILURE",
  "SAVR": "DIF",
  "RESTYPE1": "PA",
  "NAME": "SMALL BUSINESS BANK",
  "CHCLASS1": "SM",
  "COST": 5671,
  "QBFASSET": 72947,
  "CERT": 25744
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per failed bank** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://api.fdic.gov/banks/failures

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~fdic-bank-failures/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"failedSince": "2008-01-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
