# Saint Paul Building Permits

Building permits issued by the City of Saint Paul: address, permit number, type, sub-type, work type, description, estimated value, contractor name and address, status and dates. Filter by date, type, value or contractor.

## Why use it

Saint Paul publishes each permit with the contractor on it, so this is both a project feed and a contractor activity feed.

## Who it's for

- Suppliers and subcontractors finding active projects and the GC running them
- Contractors watching competitors' volume
- Investors tracking renovation by ward

## Input

| Field | What it does |
|---|---|
| `issuedSince` | **Issued on or after (YYYY-MM-DD)**. Only permits issued on or after this date. |
| `permitType` | **Permit type contains**. e.g. Building, Plumbing, Mechanical, Electrical, Demolition |
| `workType` | **Work type contains**. e.g. Remodel, New, Repair |
| `minValue` | **Minimum estimated value (USD)**. Only permits at or above this value. |
| `contractor` | **Contractor name contains**. e.g. Construction |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "issuedSince": "2025-06-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "ADDRESS": "1349 ASBURY ST",
  "STATUS": "Active/Issued",
  "ISSUEDATE": "2025-06-30T18:07:02Z",
  "EXPIRATIONDATE": "2025-12-27T00:00:00Z",
  "FINALDATE": null,
  "FOLDER_TYPE": "Building Permit",
  "SUB_TYPE": "Single Family Dwelling",
  "WORK_TYPE": "Express Repair",
  "FOLDERDESCRIPTION": "Rebuild chimney from roof up to current/code height.",
  "PIN": "222923320182",
  "latitude": "44.9819855",
  "longitude": "-93.16588025",
  "PERMITNUMBER": "25-046592",
  "EST_VALUE_OF_WORK": null,
  "STATE_VALUATION": 3995,
  "WARD": "4",
  "DISTRICT": 10,
  "CONTRACTORNAME": "TIMOTHY HOLMLUND HOLMLUND MASONRY COMPANY",
  "CONTRACTORADDRESS": "1410 2ND ST N MPLS MN 55411",
  "source": "City of Saint Paul Open Information (information.stpaul.gov)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per permit** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://services1.arcgis.com/9meaaHE3uiba0zr8/arcgis/rest/services/Building_Permits_/FeatureServer/0

Public records only. Nothing is fetched behind a login.

## Limits

- Saint Paul refreshes this layer on its own schedule; at 2026-11-03 the newest record was dated 2025-06-30. Results sort newest first.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~saint-paul-building-permits/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"issuedSince": "2025-06-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
