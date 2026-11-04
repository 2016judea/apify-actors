# FEMA Disaster Declarations

Every FEMA disaster declaration since 1953 from OpenFEMA: disaster number, state, county/area, incident type, title, declaration and incident dates, programs declared (IA, PA, HM) and closeout. Filter by state, date or incident type.

## Who it's for

- Restoration contractors and adjusters finding newly declared counties
- Lenders and insurers tracking exposure
- Grant consultants watching Hazard Mitigation and Public Assistance

## Input

| Field | What it does |
|---|---|
| `state` | **State**. Two-letter code |
| `declaredSince` | **Declared on or after (YYYY-MM-DD)**. Only declarations on or after this date. |
| `incidentType` | **Incident type**. e.g. Flood, Severe Storm, Fire, Hurricane |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "state": "MN",
  "declaredSince": "2020-01-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "femaDeclarationString": "DR-4894-MN",
  "disasterNumber": 4894,
  "state": "MN",
  "declarationType": "DR",
  "declarationDate": "2025-10-22T00:00:00.000Z",
  "fyDeclared": 2026,
  "incidentType": "Straight-Line Winds",
  "declarationTitle": "SEVERE STORMS AND STRAIGHT-LINE WINDS",
  "ihProgramDeclared": true,
  "iaProgramDeclared": false,
  "paProgramDeclared": true,
  "hmProgramDeclared": false,
  "incidentBeginDate": "2025-06-21T00:00:00.000Z",
  "incidentEndDate": "2025-06-21T00:00:00.000Z",
  "disasterCloseoutDate": null,
  "tribalRequest": true,
  "fipsStateCode": "27",
  "fipsCountyCode": "000",
  "placeCode": "36242",
  "designatedArea": "Leech Lake Indian Reservation",
  "declarationRequestNumber": "25115",
  "declarationRequestDate": "2025-08-19T00:00:00.000Z",
  "lastIAFilingDate": "2025-12-30T00:00:00.000Z",
  "incidentId": "2025070801",
  "region": 5,
  "designatedIncidentTypes": "2,W"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per declaration** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~fema-disaster-declarations/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"state": "MN", "declaredSince": "2020-01-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
