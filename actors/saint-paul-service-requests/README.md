# Saint Paul Resident Service Requests (311)

Resident service requests to the City of Saint Paul (its 311): request type, description, status, date, ward, district council and coordinates. Filter by date, type or status.

## Who it's for

- Service businesses finding neighborhoods with demand
- Council and district-council staff tracking requests
- Reporters

## Input

| Field | What it does |
|---|---|
| `requestedSince` | **Requested on or after (YYYY-MM-DD)**. Only requests on or after this date. |
| `type` | **Request type contains**. e.g. Pothole, Graffiti, Tall Grass |
| `status` | **Status contains**. e.g. Open, Closed |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "requestedSince": "2025-06-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "SERVICE_NUMBER": 5384826,
  "REQUEST_DATE": "2025-06-30T00:00:00Z",
  "WARD": null,
  "DISTRICT_COUNCIL": null,
  "STATUS": "Open",
  "REQUEST_TYPE": "Complaint",
  "REQUEST_DESCRIPTION": "Exterior",
  "SEE_CLICK_FIX_SITE": "No",
  "latitude": null,
  "longitude": null,
  "MAP_LOCATION": "(,)",
  "source": "City of Saint Paul Open Information (information.stpaul.gov)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per request** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://services1.arcgis.com/9meaaHE3uiba0zr8/arcgis/rest/services/Resident_Service_Requests/FeatureServer/0

Public records only. Nothing is fetched behind a login.

## Limits

- Saint Paul refreshes this layer on its own schedule; at 2026-11-03 the newest record was dated 2025-06-30. Results sort newest first.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~saint-paul-service-requests/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"requestedSince": "2025-06-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
