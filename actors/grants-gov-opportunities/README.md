# Grants.gov Federal Grant Opportunities

Open and forecasted federal grant opportunities from Grants.gov: opportunity number, title, agency, status, open and close dates, assistance listing numbers, and a link. Filter by keyword, agency, eligibility and funding category.

## Who it's for

- Nonprofits and grant writers finding open funding
- Universities and cities tracking forecasted grants
- Consultants building pipelines by agency

## Input

| Field | What it does |
|---|---|
| `keyword` | **Keyword**. e.g. broadband, housing, workforce |
| `status` | **Status**. forecasted/posted/closed/archived, pipe-separated. |
| `agency` | **Agency code**. e.g. HHS, DOE, USDA |
| `eligibility` | **Eligibility code**. e.g. 25 (others), 12 (nonprofits 501c3) |
| `category` | **Funding category code**. e.g. HO (housing), ED (education) |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "keyword": "housing",
  "status": "forecasted|posted",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "id": "356629",
  "number": "VA-GPD-FORECAST-FY2026-FY2028",
  "title": "GPD Grant Forecast",
  "agencyCode": "VA-HPGPDP",
  "agency": "Homeless Providers Grant and Per Diem Program",
  "openDate": "10/03/2024",
  "closeDate": "",
  "oppStatus": "forecasted",
  "docType": "forecast",
  "cfdaList": [
    "64.024"
  ],
  "url": "https://www.grants.gov/search-results-detail/356629"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per opportunity** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://api.grants.gov/v1/api/search2

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~grants-gov-opportunities/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"keyword": "housing", "status": "forecasted|posted", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
