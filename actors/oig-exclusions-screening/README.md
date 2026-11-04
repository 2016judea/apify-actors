# OIG Exclusions Check (LEIE) for Healthcare

Check people, businesses or NPIs against the HHS-OIG List of Excluded Individuals/Entities, downloaded fresh each run, or list recent exclusions by state. Returns exclusion type and reason, dates, specialty, NPI and address.

## Why use it

Medicare and Medicaid won't pay for anything an excluded person touches, so providers must screen staff and vendors monthly. This does that against the live LEIE file.

## Who it's for

- Clinics, home-care agencies and pharmacies screening staff monthly
- Credentialing and payer teams
- Healthcare staffing firms

## Input

| Field | What it does |
|---|---|
| `queries` | **Names or NPIs to check**. 'First Last', 'Last First', a business name, or a 10-digit NPI. Leave empty to list exclusions. |
| `state` | **State**. Two-letter code, to narrow matches or listings |
| `excludedSince` | **Excluded on or after (YYYY-MM-DD)**. For listing mode. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "queries": [
    "Acme Home Health LLC"
  ],
  "excludedSince": "2026-01-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "query": "Acme Home Health LLC",
  "isExcluded": false,
  "matches": [],
  "listSource": "HHS-OIG LEIE UPDATED.csv, fetched at run time"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per check or exclusion** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://oig.hhs.gov/exclusions/downloadables/UPDATED.csv

Public records only. Nothing is fetched behind a login.

## Limits

- Dates of birth in the source file are never returned.
- Exact normalized name match; confirm any hit against the OIG website before acting.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~oig-exclusions-screening/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"queries": ["Acme Home Health LLC"], "excludedSince": "2026-01-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
