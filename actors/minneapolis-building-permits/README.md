# Minneapolis Building Permits

Live building permits from the City of Minneapolis: address, permit type, work type, valuation, fees, contractor/applicant, status and dates. Filter by issue date, type, value, neighborhood or keyword.

## Why use it

Minneapolis publishes every permit it issues, usually the same day. This actor reads that feed live, pages past the 2,000-row ArcGIS cap, and returns clean rows with ISO dates and coordinates.

## Who it's for

- Contractors and suppliers finding jobs as soon as a permit is pulled (roofing, HVAC, solar, kitchens)
- Real-estate investors watching renovation and new-construction activity by neighborhood
- Lenders, insurers and analysts tracking construction value over time

## Input

| Field | What it does |
|---|---|
| `issuedSince` | **Issued on or after (YYYY-MM-DD)**. Only permits issued on or after this date. |
| `permitType` | **Permit type**. Leave empty for all. |
| `workType` | **Work type contains**. e.g. Remodel, New, Addition, Repair, Demolition |
| `minValue` | **Minimum permit value (USD)**.  |
| `neighborhood` | **Neighborhood**. Exact neighborhood name, e.g. Whittier |
| `keyword` | **Description keyword**. Matches the permit's work description, e.g. roof, solar, kitchen |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "issuedSince": "2026-10-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "APN": "0302824230011",
  "Longitude": -93.28343,
  "Latitude": 44.94422,
  "Neighborhoods_Desc": "Lyndale",
  "Wards": "8",
  "applicantName": "HOFFMAN WEBER CONSTRUCTION INC",
  "permitNumber": "BLDG1208174",
  "dwellingUnitsNew": "0",
  "dwellingUnitsEliminated": "0",
  "permitType": "Res",
  "occupancyType": "SFD",
  "workType": "Misc",
  "status": "Issued",
  "milestone": "Final Inspection",
  "permit_Value": 4792,
  "totalFees": 168.4,
  "comments": "PARTIAL ROOF REPLACMENT - REPLACING FLAT ROOF SECTION - REPLACING MODBIT ROOFING - 5 SQUARE",
  "issueDate": "2026-11-02T14:40:07Z",
  "completeDate": null,
  "applicantAddress1": "3515 48TH AVE N",
  "applicantCity": "BROOKLYN CENTER",
  "address": "3212 PLEASANT AVE",
  "ownerName": "ELIZABETH ANN PEDERSON",
  "source": "City of Minneapolis CCS_Permits (opendata.minneapolismn.gov)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per permit** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/CCS_Permits/FeatureServer/0

Public records only. Nothing is fetched behind a login.

## Limits

- City of Minneapolis only. Owner and applicant names appear exactly as the city publishes them.
- Valuation is the applicant's declared value; trade permits often show 0.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~minneapolis-building-permits/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"issuedSince": "2026-10-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
