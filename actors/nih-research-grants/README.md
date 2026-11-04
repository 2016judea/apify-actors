# NIH RePORTER Research Grants

NIH-funded research projects from RePORTER: project number, title, fiscal year, award amount with direct and indirect costs, organization and location, principal investigators, institute, activity code, dates, abstract and terms.

## Who it's for

- Life-science vendors finding labs with fresh funding
- Biotech BD and investors tracking research areas
- Grant writers and research offices benchmarking

## Input

| Field | What it does |
|---|---|
| `text` | **Search text**. Matched against title, terms and abstract. |
| `fiscalYears` | **Fiscal years (comma-separated)**. e.g. 2025,2026 |
| `orgState` | **Organization state**. Two-letter code, e.g. MN |
| `orgName` | **Organization name**. e.g. UNIVERSITY OF MINNESOTA |
| `piName` | **PI name**. Principal investigator name |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "text": "CRISPR",
  "fiscalYears": "2026",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "projectNumber": "4U19NS132301-04",
  "title": "Postnatal and Prenatal Therapeutic Base Editing for Metabolic Diseases",
  "fiscalYear": 2026,
  "awardAmount": 9996957,
  "directCost": 6893186,
  "indirectCost": 3103771,
  "organization": "CHILDREN'S HOSP OF PHILADELPHIA",
  "orgCity": "PHILADELPHIA",
  "orgState": "PA",
  "principalInvestigators": [
    "Kiran  Musunuru",
    "William H. Peranteau"
  ],
  "agency": "National Institute of Neurological Disorders and Stroke",
  "activityCode": "U19",
  "projectStart": "2023-08-01T00:00:00",
  "projectEnd": "2028-07-31T00:00:00",
  "budgetStart": "2026-08-01T00:00:00",
  "budgetEnd": "2028-07-31T00:00:00",
  "abstract": "PROJECT SUMMARY\nThe potential for the development of novel therapeutic modalities has energized the genome editing field since\nit first emerged in the 1990s and especially since the demonstration of programmable genome editing with\nCRISPR-Cas9 by multiple groups in 2012. There has been substantial progress with ex vivo therapeutic\napplications of genome editing in patients in the past few years, most notably with CAR-T immunotherapies for\ncancer and with durable treatment of hemoglobinopathies. Progress with in vivo therapeutic applications, i.e.,\nsomatic cell genome editing, has been slower due to the technical challenges inherent in the delivery of genome-\nediting tools into the body. As of the time of this writing, there are few published examples of successful genome\nediting performed in vivo in primates (including humans), with almost all examples involving somatic genome\nediting in the liver: TTR with Cas9 nuclease delivered by lipid nanoparticles (LNPs), PCSK9 and ANGPTL3\nwith adenine base editors delivered by LNPs, and PCSK9 with meganucleases delivered by adeno-associated\nvirus (AAV) vectors. The prospects for genome-editing therapies extend to before birth, with in utero genome\nediting having the potential to treat genetic diseases that result in significant morbidity and mortality before or\nshortly after birth. Although restricted to small animal models so far, in utero genome editing has proven effective\nin the liver, lungs, heart, and other organs.\nOur Overall Program seeks to build on these early successes, pursuing goals that that would be of major impact\nin advancing the field of therapeutic genome editing. Our three Research Projects seek to develop base-editing\ntherapies targeting the liver in order to treat three rare metabolic genetic diseases: phenylk
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per project** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://api.reporter.nih.gov/v2/projects/search

Public records only. Nothing is fetched behind a login.

## Limits

- Sorted by award amount. RePORTER caps a search at 15,000 results.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~nih-research-grants/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"text": "CRISPR", "fiscalYears": "2026", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
