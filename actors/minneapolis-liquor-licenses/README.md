# Minneapolis Liquor Licenses (Bars, Restaurants, Stores)

On-sale (bars, restaurants) and off-sale (liquor stores) liquor licenses in Minneapolis: license name, type, liquor type, endorsements, status, issue and expiration dates, address and coordinates.

## Why use it

A complete, current list of every licensed bar, restaurant and liquor store in the city, with license dates that show new openings.

## Who it's for

- Beverage distributors, POS and hospitality vendors building territory lists
- Spotting newly licensed venues (sort by issue date)
- Market research on nightlife by ward and neighborhood

## Input

| Field | What it does |
|---|---|
| `licenseKind` | **On-sale or off-sale**. On-sale = bars and restaurants; off-sale = liquor stores. |
| `name` | **License name contains**. e.g. Brewing |
| `issuedSince` | **Issued on or after (YYYY-MM-DD)**. Only licenses issued on or after this date. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "licenseKind": "on-sale",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "apn": "2202924240101",
  "licenseNumber": "LIC337736",
  "licenseType": "BLBrewery",
  "licenseStatus": "Pending",
  "liquorType": "On Sale",
  "issueDate": "2026-10-28T08:23:42Z",
  "expirationYear": 2027,
  "expirationDate": "2027-01-01T23:59:00Z",
  "licenseName": "Inbound Brewco",
  "address": "701 5TH ST N",
  "endorsements": "Liquor, On Sale, Taproom Class B Entertainment; Liquor, On Sale, Taproom General Entertainment",
  "ward": "5",
  "neighborhood": "North Loop",
  "lat": 44.98552,
  "long": -93.28154,
  "lastUpdateDate": "2026-10-29T18:15:19Z",
  "source": "City of Minneapolis Open Data (opendata.minneapolismn.gov)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per license** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/On_Sale_Liquor/FeatureServer/0

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~minneapolis-liquor-licenses/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"licenseKind": "on-sale", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
