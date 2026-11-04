# SEC EDGAR Full-Text Search

Search the full text of every SEC filing since 2001 with EDGAR full-text search: any phrase across 10-Ks, 8-Ks, S-1s, proxies and exhibits. Returns company, CIK, form, dates, state, SIC and a direct link to the matching document.

## Why use it

Find every company that said a phrase: 'going concern', 'material weakness', a supplier's name, a drug, a lawsuit. Boolean and exact-phrase queries work as on efts.

## Who it's for

- Short-sellers and credit analysts screening for distress language
- Sales teams finding companies that name a technology or vendor
- Lawyers and researchers tracing a term across filings

## Input

| Field | What it does |
|---|---|
| `query` | **Search query**. Exact phrases in double quotes. e.g. "going concern" |
| `forms` | **Form types (comma-separated)**. e.g. 10-K,8-K |
| `startDate` | **Filed from (YYYY-MM-DD)**. Start of filing date range. |
| `endDate` | **Filed to (YYYY-MM-DD)**. End of filing date range. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "query": "\"going concern\"",
  "forms": "10-K",
  "startDate": "2026-01-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "companies": [
    "THEGLOBE COM INC  (TGLO)  (CIK 0001066684)"
  ],
  "ciks": [
    "0001066684"
  ],
  "form": "10-K",
  "rootForms": [
    "10-K"
  ],
  "filingDate": "2026-04-01",
  "periodEnding": "2025-12-31",
  "fileType": "10-K",
  "fileDescription": "10-K",
  "accessionNumber": "0001104659-26-038019",
  "sics": [
    "7310"
  ],
  "bizStates": [
    "FL"
  ],
  "incStates": [
    "DE"
  ],
  "documentUrl": "https://www.sec.gov/Archives/edgar/data/1066684/000110465926038019/tglo-20251231x10k.htm"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per matching document** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://efts.sec.gov/LATEST/search-index

Public records only. Nothing is fetched behind a login.

## Limits

- EDGAR caps a query at 10,000 hits; narrow by form and date for more.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~sec-edgar-full-text-search/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"query": "\"going concern\"", "forms": "10-K", "startDate": "2026-01-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
