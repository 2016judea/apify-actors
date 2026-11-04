# SEC EDGAR Company Filings

List a public company's SEC filings from EDGAR by ticker, name or CIK: form type, filing and report dates, 8-K items, description and direct links to the document and filing index. Filter by form (10-K, 10-Q, 8-K, S-1, DEF 14A...) and date.

## Who it's for

- Analysts and AI agents pulling every 8-K or 10-K for a watchlist
- Compliance and IR teams monitoring peers
- Journalists tracking material events

## Input

| Field | What it does |
|---|---|
| `companies` | **Companies**. Tickers, exact company names or CIK numbers. |
| `forms` | **Form types (comma-separated)**. e.g. 10-K,10-Q,8-K. Empty for all. |
| `filedSince` | **Filed on or after (YYYY-MM-DD)**. Only filings on or after this date. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "companies": [
    "AAPL",
    "TSLA"
  ],
  "forms": "8-K,10-Q",
  "filedSince": "2025-01-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "company": "Apple Inc.",
  "cik": 320193,
  "tickers": [
    "AAPL"
  ],
  "form": "8-K",
  "filingDate": "2026-11-02",
  "reportDate": "2026-11-02",
  "acceptanceDateTime": "2026-11-02T21:30:23.000Z",
  "accessionNumber": "0000320193-26-000024",
  "description": "8-K",
  "items": "2.02,9.01",
  "size": 420455,
  "documentUrl": "https://www.sec.gov/Archives/edgar/data/320193/000032019326000024/aapl-20261102.htm",
  "indexUrl": "https://www.sec.gov/Archives/edgar/data/320193/000032019326000024/0000320193-26-000024-index.htm",
  "sic": "3571",
  "sicDescription": "Electronic Computers",
  "stateOfIncorporation": "CA"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per filing** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://data.sec.gov/submissions/

Public records only. Nothing is fetched behind a login.

## Limits

- Reads EDGAR's 'recent' submissions block (the last ~1,000 filings per company).

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~sec-edgar-filings/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"companies": ["AAPL", "TSLA"], "forms": "8-K,10-Q", "filedSince": "2025-01-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
