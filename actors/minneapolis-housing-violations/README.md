# Minneapolis Housing & Code Violations

Housing and property code violations cited by Minneapolis Regulatory Services: address, parcel, case type, violation code and description, status, processed and resolved dates. Filter by date, address, case type or open status.

## Why use it

A code violation is a property with a problem and a deadline. Investors read it as a distress signal; contractors read it as a job that has to be done.

## Who it's for

- Real-estate investors finding distressed properties
- Contractors (roofing, windows, exterior, snow) finding owners under a repair order
- Tenant advocates and researchers

## Input

| Field | What it does |
|---|---|
| `processedSince` | **Processed on or after (YYYY-MM-DD)**. Only violations processed on or after this date. |
| `address` | **Address contains**. e.g. 31ST ST |
| `violation` | **Violation description contains**. e.g. ROOF, WINDOW, PAINT, GARBAGE |
| `openOnly` | **Open violations only**. Exclude resolved violations. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "processedSince": "2026-10-01",
  "openOnly": false,
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "APN": "0102824340176",
  "address": "3733 23RD AVE S",
  "Violation_Case_Number": "CE1411105",
  "RS_Number": null,
  "Case_Type": "FIS",
  "Case_Group": "FISCOMM",
  "Case_Group_Desc": "FIS Commercial Inspection",
  "Status_Violation_Case": "Enforce",
  "Milestone_Violation_Case": "Reinspection",
  "Violation_Code": "F192",
  "Violation_Code_Description": "Maintenance Of Hood & Duct Systems",
  "Status_Violation": "",
  "Processed_Date": "2026-11-02T16:30:55Z",
  "Resolved_Date": null,
  "Source": "",
  "Resolution_Code": "",
  "Violation_Case_ID": 1902738,
  "Latitude": 44.93461,
  "Longitude": -93.2384,
  "source": "City of Minneapolis Open Data (opendata.minneapolismn.gov)"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.004 per violation** ($4 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/CaseViolations/FeatureServer/0

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~minneapolis-housing-violations/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"processedSince": "2026-10-01", "openOnly": false, "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
