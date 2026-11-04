# FDA 510(k) Medical Device Clearances

FDA 510(k) premarket clearances via openFDA: K number, device name, applicant and contact address, product code, decision and date, review panel, device class and specialty, with a link to the FDA record.

## Who it's for

- Medtech sales and regulatory consultants finding companies that just cleared a device
- Competitive intelligence by product code
- Investors tracking a company's pipeline

## Input

| Field | What it does |
|---|---|
| `decidedSince` | **Decided on or after (YYYY-MM-DD)**. Only decisions on or after this date. |
| `applicant` | **Applicant**. Exact company name |
| `deviceName` | **Device name contains**. e.g. catheter |
| `productCode` | **Product code**. 3-letter FDA product code |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "decidedSince": "2026-08-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "third_party_flag": "N",
  "city": "Bern",
  "advisory_committee_description": "Radiology",
  "address_1": "Steigerhubelstrasse 3",
  "address_2": "",
  "statement_or_summary": "Summary",
  "product_code": "QQE",
  "zip_code": "3008",
  "applicant": "Cascination AG",
  "decision_date": "2026-10-23",
  "decision_code": "SESE",
  "country_code": "CH",
  "device_name": "OTOPLAN",
  "advisory_committee": "RA",
  "contact": "Philip  Frost",
  "expedited_review_flag": "",
  "k_number": "K262080",
  "state": "",
  "date_received": "2026-06-22",
  "review_advisory_committee": "EN",
  "postal_code": "3008",
  "decision_description": "Substantially Equivalent",
  "clearance_type": "Traditional",
  "deviceClass": "2",
  "medicalSpecialty": "Radiology",
  "regulationNumber": "892.2050",
  "url": "https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K262080"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per clearance** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://api.fda.gov/device/510k.json

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~openfda-device-clearances/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"decidedSince": "2026-08-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
