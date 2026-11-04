# SEC Form 4 Insider Trades

Insider buys and sells from SEC Form 4 filings for any ticker: insider name and role, transaction date, code (open-market purchase, sale, grant, option exercise), shares, price, dollar value, holdings after, and a link to the filing.

## Why use it

Parsed straight from each Form 4's XML, one row per transaction line, with the code translated. Tick open-market only to see conviction buys and sells.

## Who it's for

- Investors and newsletters tracking insider conviction
- Quant and AI agents building insider-sentiment signals
- IR and compliance teams monitoring their own filings

## Input

| Field | What it does |
|---|---|
| `tickers` | **Tickers**. Stock tickers. |
| `filedSince` | **Filed on or after (YYYY-MM-DD)**. Only Form 4s filed on or after this date. |
| `openMarketOnly` | **Open-market buys and sells only**. Only transaction codes P and S. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "tickers": [
    "NVDA"
  ],
  "filedSince": "2026-08-01",
  "openMarketOnly": false,
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "ticker": "NVDA",
  "issuer": "NVIDIA CORP",
  "filingDate": "2026-10-13",
  "insider": "Parker Nicholas P.",
  "role": "EVP, Worldwide Field Ops",
  "transactionDate": "2026-09-09",
  "security": "Common Stock",
  "code": "A",
  "codeMeaning": "Grant/award",
  "acquiredDisposed": "A",
  "shares": 160418.0,
  "pricePerShare": 0.0,
  "value": 0.0,
  "sharesOwnedAfter": 160418.0,
  "directOrIndirect": "D",
  "accessionNumber": "0002152188-26-000007",
  "url": "https://www.sec.gov/Archives/edgar/data/1045810/000215218826000007/wk-form4a_1791925767.xml",
  "owners": [
    {
      "name": "Parker Nicholas P.",
      "isDirector": "0",
      "isOfficer": "1",
      "officerTitle": "EVP, Worldwide Field Ops",
      "isTenPercentOwner": "0"
    }
  ]
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.004 per insider transaction** ($4 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://www.sec.gov/cgi-bin/browse-edgar (Form 4 XML)

Public records only. Nothing is fetched behind a login.

## Limits

- Insiders are named exactly as on the public Form 4.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~sec-insider-trades/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"tickers": ["NVDA"], "filedSince": "2026-08-01", "openMarketOnly": false, "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
