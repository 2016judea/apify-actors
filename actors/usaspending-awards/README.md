# USAspending Federal Contracts & Grants

Search federal contract, grant, loan and IDV awards on USAspending.gov: recipient, UEI, amount, outlays, description, agency, NAICS/PSC, dates and place of performance, with a link to each award. Filter by keyword, recipient, agency, NAICS, state, amount.

## Why use it

Who the government is paying, for what, and when the work ends. The source of truth for incumbent research, teaming and competitor tracking.

## Who it's for

- GovCon BD teams finding incumbents and recompete targets by NAICS or agency
- Subcontractors finding primes that won work in their state
- Analysts and reporters tracking federal spending by recipient

## Input

| Field | What it does |
|---|---|
| `awardType` | **Award type**. Which kind of award. |
| `keywords` | **Keywords (comma-separated)**. Matched against award descriptions. |
| `recipient` | **Recipient name**. e.g. Booz Allen |
| `agency` | **Awarding agency (top tier)**. Exact name, e.g. Department of Defense |
| `naics` | **NAICS codes (comma-separated)**. e.g. 541512,541519 |
| `state` | **Place of performance state**. Two-letter code, e.g. MN |
| `minAmount` | **Minimum award amount (USD)**. Only awards at or above this amount. |
| `startDate` | **Action date from (YYYY-MM-DD)**. Awards with activity on or after this date. |
| `endDate` | **Action date to (YYYY-MM-DD)**. Awards with activity on or before this date. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "awardType": "contracts",
  "keywords": "cybersecurity",
  "startDate": "2025-10-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "Award ID": "FA862118F6251",
  "Recipient Name": "LOCKHEED MARTIN CORPORATION",
  "Recipient UEI": "KDT2YLB34NT6",
  "Award Amount": 666315748.84,
  "Total Outlays": 242708.65,
  "Description": "IGF::OT::IGF  AFSOC ACTS AWARD OF CONTRACT FOR CLS, ENGINEERING, INSTRUCTION, CYBERSECURITY, DMO",
  "Start Date": "2018-02-08",
  "End Date": "2027-01-31",
  "Awarding Agency": "Department of Defense",
  "Awarding Sub Agency": "Department of the Air Force",
  "Funding Agency": "Department of Defense",
  "Contract Award Type": "DELIVERY ORDER",
  "NAICS": {
    "code": "336413",
    "description": "OTHER AIRCRAFT PARTS AND AUXILIARY EQUIPMENT MANUFACTURING"
  },
  "PSC": {
    "code": "J069",
    "description": "MAINT/REPAIR/REBUILD OF EQUIPMENT- TRAINING AIDS AND DEVICES"
  },
  "Place of Performance State Code": "FL",
  "Place of Performance Zip5": "32825",
  "Last Modified Date": "2026-06-15 07:29:54",
  "awarding_agency_id": 1173,
  "agency_slug": "department-of-defense",
  "url": "https://www.usaspending.gov/award/CONT_AWD_FA862118F6251_9700_FA862115D6276_9700"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per award** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://api.usaspending.gov/api/v2/search/spending_by_award/

Public records only. Nothing is fetched behind a login.

## Limits

- Sorted by award amount, largest first. USAspending lags FPDS by a few days.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~usaspending-awards/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"awardType": "contracts", "keywords": "cybersecurity", "startDate": "2025-10-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
