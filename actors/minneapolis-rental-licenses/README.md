# Minneapolis Rental Licenses (Landlords)

Active rental licenses in Minneapolis: address, licensed units, tier, license dates, short-term-rental flag, and the owner and applicant names and mailing addresses the city publishes. Filter by owner, neighborhood or unit count.

## Why use it

Every rental in Minneapolis must be licensed, so this is the city's own register of who owns rental property and how many units. Search an owner to see their whole portfolio.

## Who it's for

- Property managers, insurers and contractors finding landlords by portfolio size
- Investors looking for owners of 2 to 4 unit buildings
- Tenant groups and researchers mapping ownership

## Input

| Field | What it does |
|---|---|
| `ownerName` | **Owner name contains**. e.g. LLC, or a company name |
| `neighborhood` | **Neighborhood**. Exact neighborhood name, e.g. Powderhorn Park |
| `minUnits` | **Minimum licensed units**. Only licenses with at least this many units. |
| `shortTermRentalOnly` | **Short-term rentals only**. Only licenses flagged as short-term rentals. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "minUnits": 4,
  "shortTermRentalOnly": false,
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "apn": "2602924320040",
  "rentalID": "129588",
  "licenseNumber": "LIC239862",
  "category": "CHOWNEXMPT",
  "milestone": "Active",
  "tier": "Tier 1",
  "status": "Active",
  "issueDate": "2002-04-24 00:00:00",
  "expirationDate": "2027-03-01 00:00:00",
  "address": "719 16TH ST E",
  "ownerName": "CAROLINE A HORTON",
  "ownerAddress1": "901 3RD ST N # 150",
  "ownerAddress2": null,
  "ownerCity": "MINNEAPOLIS",
  "ownerState": "MN",
  "ownerZip": "55415",
  "applicantName": "LAURA RUSS",
  "applicantAddress1": "901 N 3rd St # 150",
  "applicantAddress2": "Aeon",
  "applicantCity": "Minneapolis",
  "applicantState": "MN",
  "applicantZip": "55401",
  "licensedUnits": "99",
  "ward": "6",
  "neighborhoodDesc": "Elliot Park",
  "communityDesc": "Central",
  "policePrecinct": "1",
  "shortTermRental": "No",
  "latitude": 44.96686,
  "longitude": -93.26393,
  "source": "City of Minneapolis Open Data (opendata.minneapolismn.gov)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per license** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/Active_Rental_Licenses/FeatureServer/0

Public records only. Nothing is fetched behind a login.

## Limits

- Owner and applicant phone numbers and email addresses are deliberately omitted, even though the city file carries them.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~minneapolis-rental-licenses/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"minUnits": 4, "shortTermRentalOnly": false, "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
