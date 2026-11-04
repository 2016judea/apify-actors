# FDIC Bank Directory & Financials

Every FDIC-insured bank: name, cert, RSSD, address, holding company, regulator, charter class, total assets, deposits, net income, ROA, ROE, office count, website and coordinates. Filter by state, city, name or minimum assets.

## Who it's for

- Fintech and bank-software sales teams building target lists by asset size
- Analysts screening community banks
- M&A advisers mapping holding companies

## Input

| Field | What it does |
|---|---|
| `state` | **State**. Two-letter code, e.g. MN |
| `city` | **City**. e.g. MINNEAPOLIS |
| `name` | **Name contains**. e.g. Community |
| `minAssetsThousands` | **Minimum total assets ($ thousands)**. e.g. 1000000 for $1B. |
| `activeOnly` | **Active banks only**. Exclude closed or merged institutions. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "state": "MN",
  "activeOnly": true,
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "ZIP": "55402",
  "ACTIVE": 1,
  "BKCLASS": "SB",
  "LONGITUDE": -93.269488026048,
  "REPDTE": "06/30/2026",
  "CHRTAGNT": "OCC",
  "INSDATE": "09/14/2006",
  "WEBADDR": "www.ameriprise.com",
  "NAMEHCR": "AMERIPRISE FINANCIAL INC",
  "REGAGNT": "OCC",
  "ROA": 3.0538500392508126,
  "FED_RSSD": "3470239",
  "DEPDOM": 23942567,
  "ROE": 50.95,
  "ASSET": 25480877,
  "OFFICES": 2,
  "NETINC": 388395,
  "DEP": 23942567,
  "NAME": "Ameriprise Bank, FSB",
  "UNINUM": "445715",
  "HCTMULT": "1",
  "CITY": "Minneapolis",
  "ADDRESS": "901 3rd Avenue South",
  "CERT": 58303,
  "STALP": "MN",
  "LATITUDE": 44.972425864531,
  "ESTYMD": "09/14/2006",
  "ID": "58303",
  "fdicUrl": "https://banks.data.fdic.gov/bankfind-suite/bankfind/details/58303"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per bank** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://api.fdic.gov/banks/institutions

Public records only. Nothing is fetched behind a login.

## Limits

- Financial fields are from the latest quarterly Call Report the FDIC has loaded (REPDTE).

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~fdic-banks/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"state": "MN", "activeOnly": true, "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
