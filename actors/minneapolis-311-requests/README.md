# Minneapolis 311 Service Requests

Live 311 service requests from the City of Minneapolis: request type, subject, status, opened/closed timestamps and location. Filter by date, type or status. Years 2015 to today.

## Why use it

311 is what residents complain about, by block, as it happens: potholes, graffiti, rodents, abandoned vehicles, snow. The city publishes every case; this actor reads it live and pages past ArcGIS's row cap.

## Who it's for

- Service businesses (pest control, snow removal, junk hauling) finding where demand is right now
- Journalists and council staff tracking response times by type
- Real-estate analysts reading block-level nuisance signals

## Input

| Field | What it does |
|---|---|
| `year` | **Year**. Which year's 311 file to read. |
| `openedSince` | **Opened on or after (YYYY-MM-DD)**. Only requests opened on or after this date. |
| `type` | **Request type contains**. e.g. Pothole, Graffiti, Rodent, Abandoned Vehicle |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "year": "2026",
  "openedSince": "2026-09-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "CASEID": 201000870899,
  "ENQUIRYTYPEID": 101000367,
  "SUBJECTNAME": "Utilities Related",
  "REASONNAME": "Water",
  "TYPENAME": "Water Service Issue",
  "TITLE": "Water Service Issue",
  "OPENEDDATETIME": "2026-10-12T17:38:31Z",
  "CASESTATUS": 1,
  "CLOSEDDATETIME": null,
  "LastUpdateDate": "2026-10-13T08:05:25Z",
  "IsAccessibilityRelated": "No",
  "longitude": -93.21354227149405,
  "latitude": 44.965464253923706,
  "source": "City of Minneapolis Open Data (opendata.minneapolismn.gov)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per request** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/Public_311_2026/FeatureServer/0

Public records only. Nothing is fetched behind a login.

## Limits

- Minneapolis only. The city posts 311 cases with a lag of a few weeks; CASESTATUS is the city's numeric code.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~minneapolis-311-requests/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"year": "2026", "openedSince": "2026-09-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
