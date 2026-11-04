# US Address Geocoder with Census Tract (Free Data)

Geocode US street addresses with the official Census Bureau geocoder: matched address, latitude/longitude, state and county FIPS, census tract and block group GEOIDs, place and congressional district. One result per address.

## Who it's for

- Lenders checking CRA/LMI tracts, opportunity zones and FIPS
- Analysts joining addresses to census data
- Lead lists that need coordinates

## Input

| Field | What it does |
|---|---|
| `addresses` | **Addresses**. One full US address per line. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "addresses": [
    "350 S 5th St, Minneapolis, MN 55415",
    "1600 Pennsylvania Ave NW, Washington, DC 20500"
  ],
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "input": "350 S 5th St, Minneapolis, MN 55415",
  "matched": true,
  "matchedAddress": "350 S 5TH ST, MINNEAPOLIS, MN, 55415",
  "longitude": -93.265785679531,
  "latitude": 44.976828522245,
  "stateFips": "27",
  "state": "MN",
  "countyFips": "27053",
  "county": "Hennepin County",
  "tractGeoid": "27053126102",
  "tract": "Census Tract 1261.02",
  "blockGroupGeoid": "270531261021008",
  "place": "Minneapolis city",
  "placeGeoid": "2743000",
  "congressionalDistrict": "Congressional District 5",
  "tigerLineId": "43632452"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.001 per address** ($1 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://geocoding.geo.census.gov/geocoder/

Public records only. Nothing is fetched behind a login.

## Limits

- US addresses only. Unmatched addresses return matched=false (and are still billed as a lookup).

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~census-geocoder/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"addresses": ["350 S 5th St, Minneapolis, MN 55415", "1600 Pennsylvania Ave NW, Washington, DC 20500"], "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
