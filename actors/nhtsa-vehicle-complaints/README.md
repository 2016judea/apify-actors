# NHTSA Vehicle Owner Complaints

Owner complaints filed with NHTSA for any make, model and year: complaint date, incident date, components, crash/fire flags, injuries and deaths, and the owner's own description of what failed. Filter by component.

## Who it's for

- Lemon-law and product-liability firms finding defect patterns
- Used-car buyers and reviewers
- Automotive analysts tracking failure rates

## Input

| Field | What it does |
|---|---|
| `vehicles` | **Vehicles**. List of {make, model, year} objects. |
| `component` | **Component contains**. e.g. ELECTRICAL, STEERING, AIR BAGS |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "vehicles": [
    {
      "make": "Tesla",
      "model": "Model 3",
      "year": 2022
    }
  ],
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "odiNumber": 11499648,
  "manufacturer": "Tesla, Inc.",
  "crash": false,
  "fire": false,
  "numberOfInjuries": 0,
  "numberOfDeaths": 0,
  "dateOfIncident": "12/31/2022",
  "dateComplaintFiled": "12/31/2022",
  "vin": "5YJ3E1EC3NF",
  "components": "BACK OVER PREVENTION,FORWARD COLLISION AVOIDANCE",
  "summary": "Ghost forward collision warnings appear from time to time even tho there is no one in front of the vehicle. Sometimes when the vehicle in front of me is turning left/right the collision warning will alarm me of possible impact even tho there was no real threat for anything to happen. Also, it happens when you want to park behind a parked vehicle (it happened to me today) and alerted me of a possible crash, while i was crawling to park. I wouldn't mind these ghost warnings, but since I am using Tesla Insurance which gives monthly insurance premiums based on the safety performance of the driver (FCW is one of those and the most important one) this is always impacting me financially at the end of the month. Tesla should be forbidden to use a technology that is not perfect in order to determine the price of the insurance.",
  "vehicle": "2022 Tesla Model 3",
  "productCount": 1
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per complaint** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://api.nhtsa.gov/complaints/complaintsByVehicle

Public records only. Nothing is fetched behind a login.

## Limits

- NHTSA strips complainant identity before publishing; none is returned.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~nhtsa-vehicle-complaints/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"vehicles": [{"make": "Tesla", "model": "Model 3", "year": 2022}], "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
