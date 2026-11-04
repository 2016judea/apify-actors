# Minneapolis Police Incidents

Police incident reports from the Minneapolis Police Department: offense, description, precinct, neighborhood, public block address, dates and coordinates. Filter by year, date, offense or neighborhood.

## Why use it

Crime by block and type, straight from the city's incident file, for safety scores, site selection and reporting.

## Who it's for

- Real-estate and insurance analysts scoring blocks
- Security companies and retailers doing site selection
- Journalists tracking offense trends

## Input

| Field | What it does |
|---|---|
| `year` | **Year**. Which year's incident file to read. |
| `reportedSince` | **Reported on or after (YYYY-MM-DD)**. Only incidents reported on or after this date. |
| `offense` | **Offense/description contains**. e.g. BURG, THEFT, ASSAULT |
| `neighborhood` | **Neighborhood**. Exact neighborhood name, e.g. Whittier |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "year": "2026",
  "reportedSince": "2026-10-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "publicaddress": "0016XX 44TH AVE N",
  "caseNumber": "MP2026717565",
  "precinct": "4",
  "reportedDate": "2026-11-02T00:00:00Z",
  "reportedTime": 1012,
  "beginDate": "2026-10-29T00:00:00Z",
  "reportedDateTime": "2026-11-02T10:12:00Z",
  "beginTime": 1000,
  "offense": "THFTSW",
  "description": "THEFT BY SWINDLE",
  "UCRCode": "07",
  "enteredDate": "2026-11-02T00:00:00Z",
  "centerLong": -93.30123,
  "centerLat": 45.03545,
  "neighborhood": "Victory",
  "lastchanged": 1793577600000,
  "LastUpdateDateETL": "2026-11-03T07:50:28Z",
  "source": "City of Minneapolis Open Data (opendata.minneapolismn.gov)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per incident** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/Police_Incidents_2026/FeatureServer/0

Public records only. Nothing is fetched behind a login.

## Limits

- Addresses are block-level as MPD publishes them. No victim or suspect data exists in the source.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~minneapolis-police-incidents/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"year": "2026", "reportedSince": "2026-10-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
