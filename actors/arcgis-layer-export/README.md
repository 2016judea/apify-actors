# ArcGIS Feature Layer Exporter (No 2,000-Row Cap)

Export every row of any public ArcGIS FeatureServer or MapServer layer (city, county and state open-data portals) with a SQL where clause, field list and order. Pages past maxRecordCount, converts dates to ISO and geometry to WGS84.

## Why use it

ArcGIS returns at most maxRecordCount rows (often 1,000 or 2,000) per query and only says so in a flag most scripts ignore, so exports silently stop. This pages with resultOffset until the layer is exhausted.

## Who it's for

- Analysts pulling permits, parcels, crashes or inspections from any Hub/ArcGIS portal
- Developers who need a one-shot CSV/JSON of a layer
- AI agents that need rows, not a map

## Input

| Field | What it does |
|---|---|
| `layerUrl` | **Layer URL**. Ends in /FeatureServer/<n> or /MapServer/<n>. |
| `where` | **Where clause**. ArcGIS SQL, e.g. permitType = 'Wrecking' |
| `outFields` | **Fields**. Comma-separated, or * for all. |
| `orderBy` | **Order by**. e.g. issueDate DESC |
| `includeGeometry` | **Include geometry**. Points as latitude/longitude; polygons as rings in WGS84. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "layerUrl": "https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/CCS_Permits/FeatureServer/0",
  "where": "1=1",
  "outFields": "*",
  "orderBy": "issueDate DESC",
  "includeGeometry": false,
  "maxItems": 1000
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "OBJECTID": 275385,
  "Display": "310 ELMWOOD PL W",
  "APN": "1502824310006",
  "Longitude": -93.28288,
  "Latitude": 44.90993,
  "Neighborhoods_Desc": "Tangletown",
  "Wards": "11",
  "applicantName": "Twin City Fireplace & Stone Company",
  "permitNumber": "BLDG1208194",
  "dwellingUnitsNew": null,
  "dwellingUnitsEliminated": null,
  "permitType": "Plumbing",
  "occupancyType": " ",
  "workType": "Res",
  "status": "Issued",
  "milestone": "Inspection",
  "permit_Value": 0,
  "totalFees": 85.2,
  "comments": "remove existing gas fireplace and install new factory built gas fireplace",
  "issueDate": "2026-11-02T16:59:21Z",
  "completeDate": null,
  "fullName": "OLSON REVOCABLE FAMILY TRUST",
  "applicantAddress1": "6521 Cecilia Cir",
  "applicantCity": "Edina"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.001 per feature** ($1 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: any public ArcGIS REST layer

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~arcgis-layer-export/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"layerUrl": "https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/CCS_Permits/FeatureServer/0", "where": "1=1", "outFields": "*", "orderBy": "issueDate DESC", "includeGeometry": false, "maxItems": 1000}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
