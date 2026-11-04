# NPI Registry: Healthcare Provider Search

Search the CMS NPPES NPI Registry for doctors, clinics, pharmacies, therapists and every other US healthcare provider: NPI, name, credential, primary taxonomy, license state, practice address and phone, authorized official, enumeration date.

## Why use it

The federal registry every billing provider must be in, searched live. Phone numbers are the practice location numbers providers publish in NPPES.

## Who it's for

- Healthcare sales and recruiting teams building provider lists by specialty and city
- Payers and credentialing teams verifying an NPI
- Researchers mapping provider supply

## Input

| Field | What it does |
|---|---|
| `taxonomy` | **Specialty / taxonomy**. e.g. Physical Therapist, Dentist, Pharmacy |
| `city` | **City**. e.g. Minneapolis |
| `state` | **State**. Two-letter code |
| `zip` | **ZIP code**. 5-digit ZIP |
| `providerType` | **Provider type**. NPI-1 individuals, NPI-2 organizations. |
| `organizationName` | **Organization name**. Organization name (wildcard * allowed) |
| `lastName` | **Last name**. Individual's last name |
| `firstName` | **First name**. Individual's first name |
| `npi` | **NPI number**. Look up one NPI |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "taxonomy": "Physical Therapist",
  "city": "Minneapolis",
  "state": "MN",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "npi": "1538287404",
  "type": "Organization",
  "name": "ABBOTT NORTHWESTERN HOSPITAL",
  "status": "A",
  "enumerationDate": "2007-03-27",
  "lastUpdated": "2008-06-13",
  "authorizedOfficial": "JANE NEWMAN",
  "authorizedOfficialTitle": "Physical Therapist",
  "primaryTaxonomy": "Physical Therapist",
  "taxonomyCode": "225100000X",
  "licenseState": "MN",
  "address": "800 E 28TH ST",
  "city": "MINNEAPOLIS",
  "state": "MN",
  "zip": "55407",
  "phone": "612-863-4447"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per provider** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://npiregistry.cms.hhs.gov/api/

Public records only. Nothing is fetched behind a login.

## Limits

- The NPPES API returns at most 1,200 results per search; split by city or ZIP for more.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~npi-registry/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"taxonomy": "Physical Therapist", "city": "Minneapolis", "state": "MN", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
