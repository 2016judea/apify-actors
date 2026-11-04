# NSF Research Awards

National Science Foundation awards: award ID, title, awardee institution, city and state, obligated and estimated total amounts, start and expiry dates, PI and program officer, program and abstract, with a link to the award.

## Who it's for

- Lab-equipment and software vendors finding newly funded groups
- SBIR/STTR watchers tracking small-business awards
- Research offices benchmarking

## Input

| Field | What it does |
|---|---|
| `keyword` | **Keyword**. e.g. quantum |
| `awardeeState` | **Awardee state**. Two-letter code |
| `awardee` | **Awardee name**. Institution or company |
| `startDateFrom` | **Start date from (YYYY-MM-DD)**. Awards starting on or after this date. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "keyword": "quantum",
  "startDateFrom": "2026-01-01",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "abstractText": "The National Science Foundation (NSF), NSF EPSCoR Graduate Fellowship Program (EGFP) supports EGFP designated institutions/programs in EPSCoR jurisdictions by providing funding for graduate fellowships for eligible applicants. Institutions receive a total of three years of stipend and associated cost-of-education (COE) allowance for each NSF EPSCoR Graduate Fellow.\r\n\r\nThis award at Montana State University seeks to enhance research competitiveness and capacity through an investment in talent development. Fellow research topics will align with goals and programs supported by the NSF Directorate for Biological Sciences (BIO), and Directorate for Mathematical and Physical Sciences (MPS). Research topics and activities will focus on chemistry, physics and biology.  Fellows will pursue projects of relevance to generation of atmospheric gases by the oceans, production of methane gas by single-cell microorganisms, formation of gravitational waves by stars, and other areas of importance on Earth and beyond. The program will recruit Fellows for projects broadly focused on (i) investigation of oxygen minimum zones in oceans which host microbes that contribute to atmospheric gases, (ii) comprehensive study of routes by which White Dwarf stars produce gravitational waves, and (iii) production of methane by methanogens harvested from mangrove forests and cultured from terrestrial hot springs in Yellowstone National Park.  Participants will have multiple opportunities for research, educational, and professional interactions and will be closely mentored by a team of dedicated and experienced faculty.  The fellowship program will additionally enhance research capacity and address STEM workforce needs in Montana\u2019s rapidly growing high-technology economy. The research associated with this award is aligned with NSF's priority area of Quantum Information Science (QIS). Robust mechanisms are in place to support student success, ensuring personalized mentoring and encouraging professional development.  Apart from intensive research experience, fellows will have the opportunity to engage in teaching and mentoring of undergraduate students and interact with local industry.\r\n\r\nThis award reflects NSF's statutory mission and has been deemed worthy of support through evaluation using the Foundation's intellectual merit and broader impacts review criteria.",
  "activeAwd": "true",
  "agency": "NSF",
  "awardAgencyCode": "4900",
  "awardee": "MONTANA 
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per award** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://api.nsf.gov/services/v1/awards.json

Public records only. Nothing is fetched behind a login.

## Limits

- NSF's API returns at most 3,000 results per query.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~nsf-awards/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"keyword": "quantum", "startDateFrom": "2026-01-01", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
