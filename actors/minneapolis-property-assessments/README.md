# Minneapolis Property Assessments

The Minneapolis assessor's parcel file: address, owner as published, land/building/total value, property type, zoning, year built, area, bedrooms, bathrooms, units, construction and heating. Filter by address, neighborhood, type, value or owner.

## Why use it

The assessor's own record of every parcel in the city, with the building characteristics that listing sites hide behind a login.

## Who it's for

- Investors screening by value, units and year built
- Appraisers and tax-appeal consultants pulling comps
- Contractors targeting older housing stock

## Input

| Field | What it does |
|---|---|
| `assessmentYear` | **Assessment year**. Which assessor file to read. |
| `address` | **Address contains**. e.g. HENNEPIN AVE |
| `neighborhood` | **Neighborhood**. Neighborhood name as the assessor writes it, e.g. WHITTIER |
| `propertyType` | **Property type contains**. e.g. Residential, Apartment, Commercial |
| `minTotalValue` | **Minimum total value (USD)**. Only parcels assessed at or above this value. |
| `ownerName` | **Owner name contains**. e.g. LLC |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "assessmentYear": "2026",
  "minTotalValue": 500000,
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "ASMTYEAR": 2026,
  "TAXYR": 2027,
  "HOUSE_NO": 500,
  "ADRSTR": "11TH",
  "UNITNO": null,
  "ZIP1": 55415,
  "ADDRESSFORMATTED": "500 11TH AVE S",
  "SUBDIV": "MINNESOTA STADIUM ADDN",
  "OWNERNAME": "METROPOLITAN SPORTS FACILITIES COMMISSION",
  "MUNI": 88,
  "NEIGHBORHOOD": "DOWNTOWN EAST",
  "COMMUNITY": "DOWNTOWN",
  "ZONING": "Downtown Center",
  "PARCELAREA": 969105,
  "PROPERTYTYPE": "COMMERCIAL",
  "LANDVALUE": 77528400,
  "BUILDINGVALUE": 1150336700,
  "TOTALVALUE": 1227865100,
  "MULTIPLEUSES": "N",
  "ISEXEMPT": "Y",
  "HOMESTEAD": "N",
  "NUMBEROFBUILDINGS": 1,
  "BUILDINGUSE": "Stadium",
  "YEARBUILT": 2014,
  "BASEMENTAREA": 0,
  "ABOVEGROUNDAREA": 1750000,
  "STORIES": 1,
  "PRIMARYHEATING": "Forced Air",
  "CONSTRUCTIONTYPE": "Frame with Concrete (C)",
  "EXTERIORWALL": "METAL",
  "ROOF": "Hip",
  "GARAGESTALLS": 0,
  "TOTALBEDROOMS": 0,
  "TOTALUNITS": 0,
  "FIREPLACES": 0,
  "TOTALBATHROOMS": 0,
  "source": "City of Minneapolis Open Data (opendata.minneapolismn.gov)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per parcel** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/Assessing_Department_Parcel_Data_2026/FeatureServer/0

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~minneapolis-property-assessments/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"assessmentYear": "2026", "minTotalValue": 500000, "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
