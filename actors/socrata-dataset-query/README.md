# Socrata Open Data Query (Any City or State Portal)

Query any Socrata open-data portal (data.cityofchicago.org, data.cityofnewyork.us, data.ny.gov, data.sfgov.org...) by dataset ID with SoQL where, order, select and full-text search. Pages through results automatically.

## Who it's for

- Pulling permits, licenses, 311, crashes or inspections from hundreds of US government portals
- Scheduled exports into a warehouse
- AI agents answering questions over open data

## Input

| Field | What it does |
|---|---|
| `domain` | **Portal domain**. e.g. data.cityofchicago.org |
| `datasetId` | **Dataset ID**. The 4x4 ID in the dataset URL, e.g. ydr8-5enu (Chicago building permits). |
| `where` | **Where (SoQL)**. e.g. issue_date > '2026-10-01' |
| `order` | **Order (SoQL)**. e.g. issue_date DESC |
| `select` | **Select (SoQL)**. Columns to return; empty for all. |
| `q` | **Full-text search**. Socrata $q full-text search. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "domain": "data.cityofchicago.org",
  "datasetId": "ydr8-5enu",
  "where": "issue_date > '2026-10-01'",
  "order": "issue_date DESC",
  "maxItems": 1000
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "id": "N3003346",
  "permit_": "B200518314",
  "permit_status": "ACTIVE",
  "permit_milestone": "INSPECTION ELIGIBLE",
  "permit_type": "PERMIT \u2013 EXPRESS PERMIT PROGRAM",
  "review_type": "EXPRESS PERMIT PROGRAM",
  "application_start_date": "2026-11-02T00:00:00.000",
  "issue_date": "2026-11-02T00:00:00.000",
  "processing_time": "0",
  "street_number": "321",
  "street_direction": "E",
  "street_name": "ERIE ST",
  "work_type": "Monthly Maintenance Permit",
  "work_description": "ELECTRICAL MAINTENANCE PERMIT. OCCUPANCY: UTILTY. START DATE: 11/7/2026. END DATE: 12/7/2026. ALL WORK UNDER THIS PERMIT MUST BE PERFORMED BY EMPLOYEES OF THE LISTED ELECTRICAL CONTRACTOR. THE ELECTRICAL CONTRACTOR MUST MAINTAIN COMPLETE WRITTEN RECORDS OF ALL WORK PERFORMED UNDER THIS PERMIT AND MAKE THOSE RECORDS AVAILABLE TO THE BUILDING COMMISSIONER UPON REQUEST.",
  "building_fee_paid": "75",
  "zoning_fee_paid": "0",
  "other_fee_paid": "0",
  "subtotal_paid": "75",
  "building_fee_unpaid": "0",
  "zoning_fee_unpaid": "0",
  "other_fee_unpaid": "0",
  "subtotal_unpaid": "0",
  "building_fee_waived": "0",
  "building_fee_subtotal": "75",
  "zoning_fee_subtotal": "0",
  "other_fee_subtotal": "0",
  "zoning_fee_waived": "0",
  "other_fee_waived": "0",
  "subtotal_waived": "0",
  "total_fee": "75",
  "contact_1_type": "OWNER",
  "contact_1_name": "UNIVERSITY NORTHWESTERN",
  "contact_1_city": "CHICAGO",
  "contact_1_state": "IL",
  "contact_1_zipcode": "60610",
  "contact_2_type": "WEB APPLICANT",
  "contact_2_name": "UNIVERSITY NORTHWESTERN",
  "contact_2_city": "CHICAGO",
  "contact_2_state": "IL",
  "contact_2_zipcode": "60610",
  "contact_3_type": "ELECTRICAL CONTRACTOR",
  "contact_3_name": "ROBERT LESNICKI",
  "contact_3_city": "HOMER GLEN",
  "contact_3_state": "IL",
  "contact_3_zipcode": "60491",
  "community_area": "8",
  "census_tract": "81400",
  "ward": "2",
  "xcoordinate": "1178620.3418829716",
  "ycoordinate": "1904813.50118528",
  "latitude": "41.894113463729774",
  "longitude": "-87.61942854582708",
  "location": {
    "type": "Point",
    "coordinates": [
      -87.619428545827,
      41.89411346373
    ]
  }
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.0015 per row** ($1.5 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: any Socrata SODA endpoint

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~socrata-dataset-query/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"domain": "data.cityofchicago.org", "datasetId": "ydr8-5enu", "where": "issue_date > '2026-10-01'", "order": "issue_date DESC", "maxItems": 1000}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
