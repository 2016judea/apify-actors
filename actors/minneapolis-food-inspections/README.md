# Minneapolis Restaurant Health Inspections

Every food inspection and violation the City of Minneapolis publishes: business, address, risk level, inspection type, result, score, violation text and inspector comments. Filter by business, date, result or ZIP.

## Why use it

A failed or re-inspected kitchen is a business that needs help this week: pest control, equipment repair, food-safety training, consultants. The city publishes each inspection line by line.

## Who it's for

- Food-safety consultants and pest-control firms finding restaurants with fresh violations
- Restaurant buyers and brokers doing diligence
- Diners and reporters checking a kitchen's record

## Input

| Field | What it does |
|---|---|
| `businessName` | **Business name contains**. e.g. Taco |
| `inspectedSince` | **Inspected on or after (YYYY-MM-DD)**. Only inspections on or after this date. |
| `result` | **Inspection result contains**. e.g. Fail, Pass, Re-inspection |
| `zip` | **ZIP code**. e.g. 55408 |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "inspectedSince": "2026-09-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "HealthFacilityIDNumber": "LIC423917",
  "FacilityCategory": "RESTAURANT",
  "BusinessName": "LAINA CAFE",
  "RiskLevel": "1",
  "FullAddress": "317 LAKE ST W",
  "Unit": null,
  "City": "Minneapolis",
  "State": "MN",
  "County": "Hennepin",
  "ZipCode": "55408",
  "InspectionType": "Follow-Up",
  "InspectionResult": "Complete",
  "DateOfInspection": "2026-10-27T13:10:00Z",
  "InspectionIDNumber": 4092014,
  "FoodCodeText": null,
  "InspectorComments": null,
  "ViolationPriority": null,
  "FoodCodeItem": null,
  "YearOfInspection": 2026,
  "ViolationStatus": null,
  "ViolationPoints": 0,
  "InspectionScore": 94,
  "ViolationIDNumber": -1,
  "APN": "0302824220216",
  "Ward": "8",
  "Neighborhood": "Lyndale",
  "Latitude": 44.94811,
  "Longitude": -93.28393,
  "source": "City of Minneapolis Open Data (opendata.minneapolismn.gov)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.004 per inspection row** ($4 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/Food_Inspections/FeatureServer/0

Public records only. Nothing is fetched behind a login.

## Limits

- Minneapolis-licensed food facilities only. One row per violation line, so one inspection can return several rows.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~minneapolis-food-inspections/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"inspectedSince": "2026-09-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
