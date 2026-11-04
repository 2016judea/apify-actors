# EPA ECHO Facility Compliance & Violations

EPA-regulated facilities from ECHO: name, address, programs (air, water, hazardous waste), NAICS/SIC, inspections, quarters in violation, significant violator status, formal enforcement actions and penalties. Filter by state, city, ZIP, name, NAICS, violations or penalties.

## Who it's for

- Environmental consultants and engineering firms finding facilities in violation
- ESG and supply-chain teams screening suppliers
- Lenders and acquirers doing site diligence

## Input

| Field | What it does |
|---|---|
| `state` | **State**. Two-letter code |
| `city` | **City**. e.g. MINNEAPOLIS |
| `zip` | **ZIP code**. 5-digit ZIP |
| `name` | **Facility name contains**. e.g. foundry |
| `naics` | **NAICS code**. e.g. 331511 |
| `withViolationsOnly` | **Only facilities with violations**. Quarters in violation > 0. |
| `withPenaltiesOnly` | **Only facilities with penalties**. Total penalties > 0. |
| `activeOnly` | **Active facilities only**. Exclude inactive. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "state": "MN",
  "withViolationsOnly": true,
  "withPenaltiesOnly": false,
  "activeOnly": true,
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "FacName": " Y  MART",
  "FacState": "MN",
  "RegistryID": "110049456986",
  "FacCounty": "CASS",
  "SDWASystemTypes": "Transient non-community system",
  "FacSNCFlg": "N",
  "FacQtrsWithNC": "0",
  "FacComplianceStatus": "No Violation Identified",
  "SDWAComplianceStatus": "No Violation Identified",
  "FacInspectionCount": "0",
  "FacFormalActionCount": "0",
  "FacTotalPenalties": "$0",
  "SDWA3yrComplQtrsHistory": "_____________",
  "FacAccuracyMeters": "30000",
  "FacMyrtkUniverse": "NNN",
  "SDWISFlag": "Y",
  "GHGFlag": "N",
  "Insp5yrFlag": "0",
  "echoUrl": "https://echo.epa.gov/detailed-facility-report?fid=110049456986"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.004 per facility** ($4 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://echodata.epa.gov/echo/echo_rest_services.get_facilities

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~epa-echo-facilities/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"state": "MN", "withViolationsOnly": true, "withPenaltiesOnly": false, "activeOnly": true, "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
