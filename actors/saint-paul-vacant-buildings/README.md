# Saint Paul Vacant Buildings Register

Every building on the City of Saint Paul's vacant building register: address, parcel ID, vacant-since date, dwelling type, category, ward, district and coordinates.

## Why use it

A registered vacant building is the most direct distress signal a city publishes. The category says how serious: 1 is secured and maintained, 3 is the worst.

## Who it's for

- Investors and wholesalers finding vacant property
- Contractors and board-up services
- Neighborhood groups tracking blight

## Input

| Field | What it does |
|---|---|
| `category` | **Category**. Vacant building category (1 least to 3 most serious). Empty for all. |
| `vacantSince` | **Vacant on or after (YYYY-MM-DD)**. Only buildings registered vacant on or after this date. |
| `ward` | **Ward**. Ward number, e.g. 6 |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "ADDRESS": "1294 GRAND AVE",
  "VACANT_AS_OF": "12/31/2024",
  "DWELLING_TYPE": "Single Family Residential",
  "VB_CATEGORY": "2",
  "WARD": "3",
  "DISTRICT": 14,
  "CENSUS_TRACT": "35300",
  "PIN": "032823420018",
  "LATITUDE": "44.93985249",
  "LONGITUDE": "-93.15495124",
  "source": "City of Saint Paul Open Information (information.stpaul.gov)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.005 per vacant building** ($5 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://services1.arcgis.com/9meaaHE3uiba0zr8/arcgis/rest/services/VacantBuildings/FeatureServer/0

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~saint-paul-vacant-buildings/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
