# NHTSA Vehicle Recalls by Make, Model, Year

Every NHTSA safety recall for a list of vehicles: campaign number, component, summary, consequence, remedy, manufacturer, report date, and whether to park outside or stop driving.

## Who it's for

- Dealers and used-car buyers checking open recalls across inventory
- Fleet managers
- Auto insurers and repair shops

## Input

| Field | What it does |
|---|---|
| `vehicles` | **Vehicles**. List of {make, model, year} objects. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "vehicles": [
    {
      "make": "Honda",
      "model": "Civic",
      "year": 2020
    }
  ],
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "Manufacturer": "Honda (American Honda Motor Co.)",
  "NHTSACampaignNumber": "21V215000",
  "parkIt": false,
  "parkOutSide": false,
  "overTheAirUpdate": false,
  "ReportReceivedDate": "25/03/2021",
  "Component": "FUEL SYSTEM, GASOLINE:DELIVERY:FUEL PUMP",
  "Summary": "Honda (American Honda Motor Co.) is recalling certain 2019-2020 Acura MDX, MDX Sport Hybrid, RDX, TLX, Honda Accord, Civic Hatchback, Insight, 2019 Acura ILX, Honda Accord Hybrid, Civic Coupe, Civic Coupe Si, Civic Sedan, Civic Sedan Si, Civic Type R, Fit, HR-V, Odyssey, Passport, Pilot and Ridgeline, and 2018-2019 CR-V vehicles.  The low-pressure fuel pump inside the fuel tank may fail.",
  "Consequence": "Fuel pump failure can cause an engine stall while driving, increasing the risk of a crash.",
  "Remedy": "Honda will notify owners, and dealers will replace the fuel pump assembly, free of charge.  Owner letters were mailed May 18, 2021.  Owners may contact Honda customer service at 1-888-234-2138.  Note: This recall is an expansion of recall 20V-314.",
  "Notes": "Owners may also contact the National Highway Traffic Safety Administration Vehicle Safety Hotline at 1-888-327-4236 (TTY 1-800-424-9153), or go to www.safercar.gov.",
  "ModelYear": "2020",
  "Make": "HONDA",
  "Model": "CIVIC",
  "query": "2020 Honda Civic",
  "url": "https://www.nhtsa.gov/recalls?nhtsaId=21V215000"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per recall** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://api.nhtsa.gov/recalls/recallsByVehicle

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~nhtsa-vehicle-recalls/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"vehicles": [{"make": "Honda", "model": "Civic", "year": 2020}], "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
