# FDA Recalls (Food, Drugs, Devices)

FDA enforcement reports for food, drug and medical-device recalls via openFDA: recalling firm, product, reason, classification (I/II/III), status, distribution pattern, quantity, dates and location. Filter by type, date, class, state, firm or keyword.

## Who it's for

- Food and pharma QA teams monitoring suppliers
- Retailers and distributors checking what they carry
- Law firms and journalists tracking Class I recalls

## Input

| Field | What it does |
|---|---|
| `productType` | **Product type**. Which FDA enforcement feed. |
| `reportedSince` | **Reported on or after (YYYY-MM-DD)**. Only recalls reported on or after this date. |
| `classification` | **Classification**. Class I is the most serious. |
| `state` | **Firm state**. Two-letter code |
| `firm` | **Recalling firm**. Exact firm name |
| `keyword` | **Keyword**. Matched against product description and reason, e.g. listeria |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "productType": "food",
  "reportedSince": "2026-07-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "status": "Ongoing",
  "city": "Vernon",
  "state": "CA",
  "country": "United States",
  "classification": "Class II",
  "product_type": "Food",
  "event_id": "99727",
  "recalling_firm": "El Ruisenor De Mexico, Inc.",
  "address_1": "5512 S Santa Fe Ave",
  "address_2": "",
  "postal_code": "90058-3524",
  "voluntary_mandated": "Voluntary: Firm initiated",
  "initial_firm_notification": "Two or more of the following: Email, Fax, Letter, Press Release, Telephone, Visit",
  "distribution_pattern": "Recalling firm distributes primarily to California customers both retail and wholesale. Additional distribution to limited customers in Hawaii, Illinois, Kansas, Nevada, Oregon, and Washington.",
  "recall_number": "H-0130-2027",
  "product_description": "Jovy Gummy Worms Neon; packaged in 1lb plastic units. UPC 712199083411",
  "product_quantity": "521 pounds",
  "reason_for_recall": "undeclared allergen ingredient (Red#40, Yellow#5, Yellow#6, Blue#1)",
  "recall_initiation_date": "20260824",
  "center_classification_date": "20261020",
  "report_date": "20261028",
  "code_info": "lot: 6156",
  "more_code_info": "",
  "productType": "food"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per recall** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://api.fda.gov/{food,drug,device}/enforcement.json

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~openfda-recalls/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"productType": "food", "reportedSince": "2026-07-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
