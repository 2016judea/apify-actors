# Hennepin County Property Records (Minneapolis Metro)

Parcel records for every property in Hennepin County, MN (Minneapolis and 44 suburbs): owner and taxpayer as published, address, property type, market and taxable value, last sale price and date, taxes, delinquency year, year built, lot area and coordinates.

## Why use it

The county's own parcel file, one row per property, with the tax and sale fields listing sites don't show. Search by street, city, parcel ID or owner.

## Who it's for

- Investors and wholesalers pulling owner, value and last sale for a street or city
- Title, lending and insurance teams verifying a parcel
- Tax-delinquency screening (EARLIEST_DELQ_YR)

## Input

| Field | What it does |
|---|---|
| `street` | **Street name starts with**. e.g. LYNDALE AVE S (the county writes streets in capitals) |
| `houseNumber` | **House number**. Exact house number. |
| `city` | **City**. e.g. MINNEAPOLIS, EDINA, BLOOMINGTON |
| `pid` | **Parcel ID (PID)**. 13-digit Hennepin PID |
| `ownerName` | **Owner name contains**. e.g. LLC |
| `delinquentOnly` | **Tax-delinquent only**. Only parcels with a delinquent tax year. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "street": "LYNDALE AVE S",
  "delinquentOnly": false,
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "PID": "0302724220019",
  "PID_TEXT": "(19)",
  "HOUSE_NO": 7845,
  "FRAC_HOUSE_NO": "",
  "STREET_NM": "LYNDALE AVE S",
  "CONDO_NO": "",
  "ZIP_CD": "55420",
  "MUNIC_NM": "BLOOMINGTON",
  "OWNER_NM": "KEATS BLOOMINGTON LLC",
  "TAXPAYER_NM": "KEATS BLOOMINGTON LLC",
  "TAXPAYER_NM_1": "C/O BENJAMIN B SMITH",
  "TAXPAYER_NM_2": "PO BOX 666",
  "TAXPAYER_NM_3": "WAYZATA MN 55391",
  "BUILD_YR": "1955",
  "SALE_DATE": "",
  "SALE_PRICE": 0,
  "SALE_CODE_NAME": "",
  "PARCEL_AREA": 68458.69654729,
  "MKT_VAL_TOT": 4305000,
  "TAXABLE_VAL_TOT": 4305000,
  "TAX_TOT": 137678.76,
  "NET_TAX_PD": 68839.38,
  "EARLIEST_DELQ_YR": "",
  "PR_TYP_NM1": "COMMERCIAL-PREFERRED",
  "HMSTD_CD1": "N",
  "LAND_MV1": 1819900,
  "BLDG_MV1": 2485100,
  "TOTAL_MV1": 4305000,
  "SCHOOL_DIST_NO": "271",
  "ABBREV_ADDN_NM": "DONALD K SMITH 1ST ADDN",
  "LOT": "001",
  "BLOCK": "001",
  "LAT": 44.859683,
  "LON": -93.287412,
  "source": "Hennepin County GIS, LAND_PROPERTY parcels (gis.hennepin.us)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per parcel** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://gis.hennepin.us/arcgis/rest/services/HennepinData/LAND_PROPERTY/MapServer/1

Public records only. Nothing is fetched behind a login.

## Limits

- Hennepin County only. Owner and taxpayer names are the county's published fields.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~hennepin-county-property-records/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"street": "LYNDALE AVE S", "delinquentOnly": false, "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
