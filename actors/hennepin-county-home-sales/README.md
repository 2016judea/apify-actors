# Hennepin County Recorded Property Sales

Recent recorded property sales in Hennepin County, MN (Minneapolis and suburbs): sale price, sale month, deed type, address, property type, market value, year built and coordinates. Filter by city, ZIP, price or sale month.

## Why use it

Minnesota is a disclosure state, so the actual price paid is public. This reads the county's last recorded sale per parcel, newest first, which is the comp set appraisers and investors need.

## Who it's for

- Investors and agents pulling sold comps by city or ZIP
- Appraisers and lenders checking sale-to-value ratios
- Market reporters tracking prices month by month

## Input

| Field | What it does |
|---|---|
| `soldSince` | **Sold in or after month (YYYYMM)**. e.g. 202608 |
| `city` | **City**. e.g. MINNEAPOLIS |
| `zip` | **ZIP code**. e.g. 55406 |
| `minPrice` | **Minimum sale price (USD)**. Only sales at or above this price. |
| `maxPrice` | **Maximum sale price (USD)**. Only sales at or below this price. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "soldSince": "202608",
  "minPrice": 100000,
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "PID": "0102824440036",
  "PID_TEXT": "(36)",
  "HOUSE_NO": 3647,
  "FRAC_HOUSE_NO": "",
  "STREET_NM": "28TH AVE S",
  "CONDO_NO": "",
  "ZIP_CD": "55406",
  "MUNIC_NM": "MINNEAPOLIS",
  "OWNER_NM": "CARINA PATON & ISAAC OLSON",
  "TAXPAYER_NM": "CARINA PATON & ISAAC OLSON",
  "TAXPAYER_NM_1": "3647 28TH AVE S",
  "TAXPAYER_NM_2": "MINNEAPOLIS MN   55406",
  "TAXPAYER_NM_3": "",
  "BUILD_YR": "1953",
  "SALE_DATE": "202609",
  "SALE_PRICE": 310000,
  "SALE_CODE_NAME": "WARRANTY DEED",
  "PARCEL_AREA": 5067.97941168,
  "MKT_VAL_TOT": 285200,
  "TAXABLE_VAL_TOT": 264318,
  "TAX_TOT": 4121.6,
  "NET_TAX_PD": 2060.8,
  "EARLIEST_DELQ_YR": "",
  "PR_TYP_NM1": "RESIDENTIAL",
  "HMSTD_CD1": "H",
  "LAND_MV1": 112000,
  "BLDG_MV1": 173200,
  "TOTAL_MV1": 285200,
  "SCHOOL_DIST_NO": "001",
  "ABBREV_ADDN_NM": "PALMERS ADDN TO MPLS",
  "LOT": "018",
  "BLOCK": "015",
  "LAT": 44.936352,
  "LON": -93.231752,
  "source": "Hennepin County GIS, LAND_PROPERTY parcels (gis.hennepin.us)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per sale** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://gis.hennepin.us/arcgis/rest/services/HennepinData/LAND_PROPERTY/MapServer/1

Public records only. Nothing is fetched behind a login.

## Limits

- The county holds the LAST sale per parcel, so earlier sales of the same parcel are not returned.
- Sale month (YYYYMM) is the county's precision.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~hennepin-county-home-sales/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"soldSince": "202608", "minPrice": 100000, "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
