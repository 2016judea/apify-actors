# SEC Company Financials (XBRL)

Annual or quarterly financials for any US-listed company from SEC XBRL data: revenue, gross profit, operating and net income, diluted EPS, assets, liabilities, equity, cash, operating cash flow, capex, long-term debt and shares.

## Why use it

Numbers as the company tagged them in its own 10-K/10-Q, one row per period, no scraping of finance portals.

## Who it's for

- Analysts and AI agents building comps and screens
- Lenders checking a borrower's reported financials
- Founders benchmarking public competitors

## Input

| Field | What it does |
|---|---|
| `tickers` | **Tickers**. Stock tickers or CIKs. |
| `period` | **Period**. Annual (10-K) or quarterly (10-Q). |
| `years` | **Years**. How many years back. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "tickers": [
    "MSFT",
    "GOOGL"
  ],
  "period": "annual",
  "years": 5,
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "ticker": "MSFT",
  "company": "MICROSOFT CORP",
  "cik": 789019,
  "periodEnd": "2026-06-30",
  "period": "annual",
  "revenue": 331839000000,
  "filed": "2026-07-29",
  "form": "10-K",
  "fiscalYear": 2026,
  "netIncome": 133749000000,
  "operatingIncome": 155237000000,
  "grossProfit": 225465000000,
  "eps": 17.95,
  "totalAssets": 758376000000,
  "totalLiabilities": 315989000000,
  "equity": 442387000000,
  "cash": 20935000000,
  "operatingCashFlow": 182935000000,
  "capex": 115948000000,
  "longTermDebt": 31067000000,
  "sharesOutstanding": 7427000000
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.005 per financial period** ($5 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://data.sec.gov/api/xbrl/companyfacts/

Public records only. Nothing is fetched behind a login.

## Limits

- Quarterly rows cover discrete quarters reported on 10-Q; Q4 is in the annual figure.
- Companies that use non-standard tags may leave a metric blank.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~sec-company-financials/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"tickers": ["MSFT", "GOOGL"], "period": "annual", "years": 5, "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
