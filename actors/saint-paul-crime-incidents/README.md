# Saint Paul Crime Incidents

Crime incident reports from the Saint Paul Police Department: case number, date, time, incident type, block, neighborhood, police grid and call disposition. Filter by date, incident or neighborhood.

## Who it's for

- Safety scoring for real estate and insurance
- Site selection
- Journalism and research

## Input

| Field | What it does |
|---|---|
| `since` | **On or after (YYYY-MM-DD)**. Only incidents on or after this date. |
| `incident` | **Incident contains**. e.g. Burglary, Theft, Auto |
| `neighborhood` | **Neighborhood name contains**. e.g. Frogtown |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "since": "2026-09-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "CASE_NUMBER": 26199331,
  "DATE": "2026-11-03T17:49:00Z",
  "TIME": null,
  "CODE": 600,
  "INCIDENT_TYPE": "THEFT EXCEPT AUTO THEFT",
  "INCIDENT": "Theft",
  "POLICE_GRID_NUMBER": 112,
  "NEIGHBORHOOD_NUMBER": 5,
  "NEIGHBORHOOD_NAME": "5 - Payne/Phalen",
  "BLOCK": "3XX GROVE ST",
  "CALL_DISPOSITION_CODE": "R",
  "CALL_DISPOSITION": "Report Written",
  "source": "City of Saint Paul Open Information (information.stpaul.gov)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per incident** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://services1.arcgis.com/9meaaHE3uiba0zr8/arcgis/rest/services/Crime_Incident_Report_-_Dataset/FeatureServer/0

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~saint-paul-crime-incidents/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"since": "2026-09-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
