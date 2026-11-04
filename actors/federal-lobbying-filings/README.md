# Federal Lobbying Disclosure Filings (LD-2)

Lobbying Disclosure Act filings from the Senate/House LDA database: registrant (lobbying firm), client, quarter, income or expenses, issue areas, specific issues lobbied, government entities contacted and lobbyists named. Filter by client, registrant, year or issue.

## Who it's for

- Public-affairs teams tracking who lobbies on their issue
- Journalists following money into an agency
- Sales teams finding companies with active policy spend

## Input

| Field | What it does |
|---|---|
| `clientName` | **Client name**. e.g. Target |
| `registrantName` | **Registrant (firm) name**. e.g. Akin Gump |
| `filingYear` | **Filing year**. e.g. 2026 |
| `issueCode` | **Specific issue text**. Words in the specific-issues field |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "clientName": "Target",
  "filingYear": 2026,
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "filingUuid": "9300b2d8-2865-47a7-9814-332d0def57b1",
  "filingType": "3rd Quarter - Report",
  "filingYear": 2026,
  "period": "3rd Quarter (July 1 - Sep 30)",
  "posted": "2026-10-20T20:41:24-04:00",
  "income": null,
  "expenses": null,
  "registrant": "JGB & ASSOCIATES, LLC",
  "client": "CORNERSTONE GOVERNMENT AFFAIRS OBO TARGET CORPORATION",
  "clientState": "MN",
  "clientDescription": "General merchandise and grocery retail store and online shopping",
  "issues": [
    "Defense",
    "Banking",
    "Consumer Issues/Safety/Products",
    "Trade (domestic/foreign)",
    "Taxation/Internal Revenue Code"
  ],
  "specificIssues": [
    "Issues related to amending the National Defense Authorization Act (S. 4784).",
    "Issues related to S. 1535, the Common Cents Act; issues related to surveillance pricing.",
    "Issues surrounding online data and privacy, Kids Online Safety Act (S. 1748), the Kids Internet and Digital Safety Act (HR 7757) and the Children and Teens Online Privacy Protection Act (S. 836 and HR 6291); legislation related to Organized Retail Crime, S. 1404.",
    "Issues related to trade tariffs and refunds.",
    "Issues related to innovation, competition and consumer goods; tariff policies; general trade provisions and tariffs."
  ],
  "governmentEntities": [
    "HOUSE OF REPRESENTATIVES",
    "SENATE"
  ],
  "lobbyists": [
    "JOHN BUSCHER"
  ],
  "documentUrl": "https://lda.gov/filings/public/filing/9300b2d8-2865-47a7-9814-332d0def57b1/print/"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per filing** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://lda.gov/api/v1/filings/

Public records only. Nothing is fetched behind a login.

## Limits

- Lobbyist names are the registered lobbyists listed on the public filing.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~federal-lobbying-filings/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"clientName": "Target", "filingYear": 2026, "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
