# IRS Nonprofits & Foundations by State

Every tax-exempt organization the IRS lists for a state (Exempt Organizations Business Master File): EIN, name, address, 501(c) subsection, foundation type, NTEE category, ruling year, assets, income and revenue. Filter by name, city, NTEE, revenue or private foundations.

## Why use it

The IRS master list, read fresh from irs.gov each run. Tick 'private foundations only' and sort by revenue to get a state's grantmakers.

## Who it's for

- Grant writers and nonprofits finding funders (private foundations) near them
- Vendors selling to nonprofits by size and cause (NTEE)
- Researchers sizing a state's nonprofit sector

## Input

| Field | What it does |
|---|---|
| `state` | **State**. Two-letter code |
| `name` | **Name contains**. e.g. FOUNDATION |
| `city` | **City**. Exact city in capitals, e.g. MINNEAPOLIS |
| `nteePrefix` | **NTEE code prefix**. e.g. T (philanthropy), P (human services), B2 (schools) |
| `minRevenue` | **Minimum revenue (USD)**. From the latest return the IRS processed. |
| `privateFoundationsOnly` | **Private foundations only**. Foundation codes 02, 03, 04. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "state": "MN",
  "minRevenue": 1000000,
  "privateFoundationsOnly": false,
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "ein": "383952644",
  "name": "MAYO CLINIC GROUP RETURN",
  "inCareOf": null,
  "street": "PO BOX 4007",
  "city": "ROCHESTER",
  "state": "MN",
  "zip": "55903-4007",
  "subsection": "501(c)(3)",
  "foundationCode": "16",
  "foundationType": "Publicly supported (gross receipts)",
  "nteeCode": "E21",
  "nteeCategory": "Health",
  "rulingYear": "2014",
  "taxPeriod": "202412",
  "assets": 17859698606.0,
  "income": 14918955280.0,
  "revenue": 14891458272.0,
  "deductible": true,
  "irsLookup": "https://apps.irs.gov/app/eos/details/?ein=383952644"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per organization** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://www.irs.gov/pub/irs-soi/eo_{state}.csv

Public records only. Nothing is fetched behind a login.

## Limits

- Sorted by revenue, largest first. Financials are from the organization's latest return in the IRS file.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~irs-exempt-organizations/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"state": "MN", "minRevenue": 1000000, "privateFoundationsOnly": false, "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
