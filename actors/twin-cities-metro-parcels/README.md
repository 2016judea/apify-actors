# Twin Cities Metro Parcels (7 Counties)

Parcel records for the 7-county Twin Cities metro on one schema: address, owner as published, land/building/total value, taxes, use class, home style, finished sq ft, year built, units, last sale date and value.

## Why use it

One schema across seven counties, from the Metropolitan Council's regional parcel dataset, so a search for 'homes built before 1950 in Ramsey County with a sale since 2024' is one input.

## Who it's for

- Investors screening the whole metro by value, age and use
- Contractors targeting a housing vintage by city
- Analysts comparing counties on one schema

## Input

| Field | What it does |
|---|---|
| `county` | **County**. Which county to read. |
| `city` | **City**. e.g. SAINT PAUL, ROSEVILLE (capitals) |
| `street` | **Street name contains**. e.g. GRAND |
| `zip` | **ZIP code**. e.g. 55105 |
| `builtBefore` | **Built before year**. Only parcels built before this year. |
| `minValue` | **Minimum total value (USD)**. Only parcels at or above this value. |
| `ownerName` | **Owner name contains**. e.g. LLC |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "county": "Ramsey",
  "city": "SAINT PAUL",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "COUNTY_PIN": "312922130021",
  "STATE_PIN": "27123-312922130021",
  "ANUMBERPRE": null,
  "ANUMBER": 235,
  "ANUMBERSUF": null,
  "ST_PRE_MOD": null,
  "ST_PRE_DIR": null,
  "ST_PRE_TYP": null,
  "ST_PRE_SEP": null,
  "ST_NAME": "12th",
  "ST_POS_TYP": "Street",
  "ST_POS_DIR": "East",
  "ST_POS_MOD": null,
  "SUB_TYPE1": null,
  "SUB_ID1": null,
  "SUB_TYPE2": null,
  "SUB_ID2": null,
  "ZIP": "55101",
  "ZIP4": null,
  "CTU_NAME": "Saint Paul",
  "CTU_ID_TXT": "02396511",
  "POSTCOMM": "St Paul",
  "CO_CODE": "27123",
  "CO_NAME": "Ramsey",
  "STATE_CODE": "MN",
  "LOT": "TRACT A",
  "BLOCK": null,
  "PLAT_NAME": "REGISTERED LAND SURVEY 609",
  "OWNER_NAME": "HEALTH PARTNERS REAL ESTATE",
  "OWNER_MORE": null,
  "OWN_ADD_L1": "8170 33RD AVE S",
  "OWN_ADD_L2": null,
  "OWN_ADD_L3": "BLOOMINGTON MN 55425-4516",
  "OWN_ADD_L4": null,
  "TAX_NAME": "COUNTY OF RAMSEY",
  "TAX_ADD_L1": "121 7TH PL STE 2200",
  "TAX_ADD_L2": null,
  "TAX_ADD_L3": "SAINT PAUL MN 55101-2146",
  "TAX_ADD_L4": null,
  "LANDMARK": "Ramsey County Medical Examiner",
  "HOMESTEAD": "No",
  "ACRES_POLY": 17.4,
  "ACRES_DEED": 17.5,
  "EMV_LAND": 15713300,
  "EMV_BLDG": 301000000,
  "EMV_TOTAL": 316713300,
  "TAX_YEAR": 2026,
  "MKT_YEAR": 2025,
  "TAX_CAPAC": null,
  "TOTAL_TAX": null,
  "SPEC_ASSES": null,
  "USECLASS1": "5E HOSPITAL-PUBLIC",
  "USECLASS2": null,
  "USECLASS3": null,
  "USECLASS4": null,
  "MULTI_USES": "No",
  "TAX_EXEMPT": "Y",
  "XUSECLASS1": "5E HOSPITAL-PUBLIC",
  "XUSECLASS2": null,
  "XUSECLASS3": null,
  "XUSECLASS4": null,
  "DWELL_TYPE": null,
  "HOME_STYLE": null,
  "FIN_SQ_FT": null,
  "GARAGE": "No",
  "GARAGESQFT": null,
  "BASEMENT": "Unknown",
  "HEATING": null,
  "COOLING": null,
  "YEAR_BUILT": 1963,
  "NUM_UNITS": null,
  "SALE_DATE": null,
  "SALE_VALUE": null,
  "GREEN_ACRE": "No",
  "OPEN_SPACE": "No",
  "AG_PRESERV": "No",
  "AGPRE_ENRD": null,
  "AGPRE_EXPD": null,
  "ABB_LEGAL": "REGISTERED LAND SURVEY 609 TRACT A",
  "EDIT_DATE": "2026-04-08T12:17:40Z",
  "EXP_DATE": "2026-09-25T00:00:00Z",
  "OWNERSHIP": "Unknown",
  "SCHOOL_DST": "01-0625",
  "WSHD_DST": "Capitol Region WSD",
  "SECTION": 31,
  "TOWNSHIP": 29,
  "RANGE": 22,
  "RANGE_DIR": 0,
  "PRIN_MER": 4,
  "PIN": "123-312922130021",
  "VIEWID": 4110934,
  "source": "Metropolitan Council regional parcel dataset (MetroGIS)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per parcel** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://arcgis.metc.state.mn.us/data1/rest/services/parcels/Parcels/FeatureServer

Public records only. Nothing is fetched behind a login.

## Limits

- Refreshed by the Metropolitan Council on its own schedule (quarterly or so), not daily.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~twin-cities-metro-parcels/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"county": "Ramsey", "city": "SAINT PAUL", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
