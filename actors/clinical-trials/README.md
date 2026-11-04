# ClinicalTrials.gov Study Search

Search ClinicalTrials.gov studies by condition, intervention, sponsor, location and status: NCT ID, titles, status, phases, enrollment, start and completion dates, sponsor and collaborators, sites, and summary.

## Who it's for

- CROs and site networks finding sponsors recruiting in their area
- Pharma competitive intelligence
- Patient-recruitment and research teams

## Input

| Field | What it does |
|---|---|
| `condition` | **Condition**. e.g. obesity |
| `intervention` | **Intervention**. e.g. semaglutide |
| `sponsor` | **Sponsor**. e.g. Novo Nordisk |
| `location` | **Location**. City, state or country, e.g. Minneapolis |
| `status` | **Overall status**. e.g. RECRUITING, COMPLETED, NOT_YET_RECRUITING |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "condition": "obesity",
  "status": "RECRUITING",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "nctId": "NCT07331974",
  "title": "Efficacy and Safety of Akkermansia Muciniphila AKM Lab-01 for Overweight and Obesity",
  "officialTitle": "A Randomized, Double-blind, Placebo-controlled Trial to Access the Efficacy and Safety of Akkermansia Muciniphila AKM Lab-01 in Participents With Overweigh and Obesity",
  "status": "RECRUITING",
  "startDate": "2026-06-18",
  "primaryCompletion": "2027-03-31",
  "lastUpdate": "2026-10-09",
  "phases": [
    "NA"
  ],
  "studyType": "INTERVENTIONAL",
  "enrollment": 200,
  "conditions": [
    "Overweight , Obesity"
  ],
  "interventions": [
    "AKM Lab-01",
    "Placebo"
  ],
  "leadSponsor": "Moon (Guangzhou) Biotechnology Co., Ltd.",
  "sponsorClass": "INDUSTRY",
  "collaborators": [],
  "locationCount": 1,
  "locations": [
    "Guangzhou Huangpu District People's Hospital, Guangzhou, Guangdong, China"
  ],
  "summary": "This study is designed as a preliminary investigation to evaluate the weight-loss efficacy and safety of AKM Lab-01 in an overweight or obese population. It is an interventional, radomized, double-blind, placebo-controlled clinical trial. Participants who meet the eligibility criteria will be randomly assigned to receive AKM Lab-01 or a matching placebo. The intervention will be administered once daily for 3 months. Baseline metrics, along with blood, urine, and stool samples, will be collected from participants, before and after the AKM Lab-01 intervention. The analysis will focus on changes in body weight, blood lipids, blood glucose, and gut metagenomic profiles (from stool samples). Furthermore, metabolomic analysis of blood and stool samples will be conducted to explore the potential machanisms through which AMK Lab-01 influences body weight.",
  "url": "https://clinicaltrials.gov/study/NCT07331974"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per study** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://clinicaltrials.gov/api/v2/studies

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~clinical-trials/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"condition": "obesity", "status": "RECRUITING", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
