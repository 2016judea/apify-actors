# CMS Hospital Star Ratings & Quality

Medicare Care Compare data for every US hospital: CMS ID, name, address, phone, type, ownership, emergency services, overall star rating, and mortality, safety, readmission, patient-experience and timeliness measure counts.

## Who it's for

- Health-tech and med-device sales teams building hospital lists
- Patients and journalists comparing quality
- Analysts studying ownership vs ratings

## Input

| Field | What it does |
|---|---|
| `state` | **State**. Two-letter code |
| `city` | **City**. City in capitals |
| `hospitalType` | **Hospital type**. e.g. Acute Care Hospitals, Critical Access Hospitals |
| `minRating` | **Minimum overall star rating**. 1-5 |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "state": "MN",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "facility_id": "240001",
  "facility_name": "NORTH MEMORIAL HEALTH HOSPITAL",
  "address": "3300 OAKDALE NORTH",
  "citytown": "ROBBINSDALE",
  "state": "MN",
  "zip_code": "55422",
  "countyparish": "HENNEPIN",
  "telephone_number": "(763) 520-5200",
  "hospital_type": "Acute Care Hospitals",
  "hospital_ownership": "Voluntary non-profit - Private",
  "emergency_services": "Yes",
  "meets_criteria_for_birthing_friendly_designation": "Y",
  "hospital_overall_rating": "1",
  "mort_group_measure_count": "8",
  "count_of_facility_mort_measures": "8",
  "count_of_mort_measures_better": "0",
  "count_of_mort_measures_no_different": "8",
  "count_of_mort_measures_worse": "0",
  "safety_group_measure_count": "8",
  "count_of_facility_safety_measures": "6",
  "count_of_safety_measures_better": "1",
  "count_of_safety_measures_no_different": "4",
  "count_of_safety_measures_worse": "1",
  "readm_group_measure_count": "11",
  "count_of_facility_readm_measures": "10",
  "count_of_readm_measures_better": "0",
  "count_of_readm_measures_no_different": "8",
  "count_of_readm_measures_worse": "2",
  "pt_exp_group_measure_count": "15",
  "count_of_facility_pt_exp_measures": "15",
  "te_group_measure_count": "10",
  "count_of_facility_te_measures": "8",
  "careCompareUrl": "https://www.medicare.gov/care-compare/details/hospital/240001"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per hospital** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://data.cms.gov/provider-data/dataset/xubh-q36u

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~cms-hospital-ratings/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"state": "MN", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
