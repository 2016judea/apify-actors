# CPSC Consumer Product Recalls

Consumer product recalls from the US Consumer Product Safety Commission: recall number and date, title, products and units, hazards, remedies, manufacturers, retailers, importers, countries of manufacture, injuries and images.

## Who it's for

- Marketplace sellers and retailers checking listings against recalls
- Importers and sourcing teams screening manufacturers
- Product-liability lawyers and journalists

## Input

| Field | What it does |
|---|---|
| `recalledSince` | **Recalled on or after (YYYY-MM-DD)**. Only recalls on or after this date. |
| `keyword` | **Product name contains**. e.g. stroller, heater |
| `manufacturer` | **Manufacturer contains**. Manufacturer name |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "recalledSince": "2026-06-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "recallNumber": "27055",
  "recallDate": "2026-10-29",
  "title": "Bodum USA Recalls 5.9 Million French Press Coffee Makers with Replaceable Glass Carafes Due to Risk of Serious Burn Injury",
  "description": "This recall involves Bodum 8-cup and 12-cup Bistro, Brazil, Caffettiera, Chambord, Crema, Java, Jesper, and Kenya model French Press coffee makers with replaceable glass carafes. The Bodum name appears on the frame and inner lid of most models, and is engraved, along with product warnings, on the glass carafes. Additional photos and model-identifying information are available on the recall website.\n\n",
  "url": "https://cpsc.gov/Recalls/2027/Bodum-USA-Recalls-5-9-Million-French-Press-Coffee-Makers-with-Replaceable-Glass-Carafes-Due-to-Risk-of-Serious-Burn-Injury",
  "products": [
    "Bodum French Press coffee makers with 8-cup and 12-cup replaceable glass carafes (Bistro, Brazil, Caffettiera, Chambord, Crema, Java, Jesper, and Kenya models)"
  ],
  "units": [
    "5.9 million"
  ],
  "hazards": [
    "The carafe can unexpectedly break during use if the glass carafe is damaged or cracked, including by use of a metal spoon to stir the coffee, posing a risk of serious burn injuries."
  ],
  "remedies": [
    "Consumers should stop using metal spoons or utensils to stir coffee in the glass carafe immediately and contact Bodum to receive a plastic Bodum stirring spoon and warning label. The label reminds consumers not to use cracked or damaged carafes and not to use metal spoons to stir contents in the glass carafe in order to avoid damaging the glass, which can lead to breakage during use."
  ],
  "remedyOptions": [
    "Repair"
  ],
  "manufacturers": [],
  "retailers": [
    "Sold At:\nTarget, Walmart, and coffee and home goods stores nationwide and online at Bodum.com, Amazon.com, Target.com, Walmart.com and other online retailers from 1974 through October 2026 for about $15 to $65."
  ],
  "importers": [
    "Bodum USA, Inc., of New York, New York"
  ],
  "distributors": [],
  "manufacturerCountries": [
    "Portugal",
    "Thailand"
  ],
  "injuries": [
    "Bodum USA has identified 70 reports of carafes breaking during use, including 48 reports of burns to consumers"
  ],
  "consumerContact": "Bodum USA toll-free at 888-879-8213 from 8 a.m. to 5 p.m. ET Monday through Friday, email at Bodum3302@sedgwick.com, or online at www.bodumfrenchpressrecall.expertinquiry.com or www.bodum.com  and click on \u201cRecall Information\u201d for more inform
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per recall** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://www.saferproducts.gov/RestWebServices/Recall

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~cpsc-product-recalls/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"recalledSince": "2026-06-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
