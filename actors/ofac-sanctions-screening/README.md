# OFAC Sanctions Screening (SDN List)

Screen a list of people, companies or vessels against the US Treasury OFAC SDN list and its aliases, downloaded fresh each run. Returns, per name, whether there is a potential match, the score, and the SDN entry, type, programs and remarks.

## Why use it

Fuzzy matching on normalized names (punctuation and legal suffixes stripped, word order ignored) against every SDN name and alias. A potential match is a reason to review, not a determination.

## Who it's for

- Fintechs, marketplaces and exporters screening counterparties
- Compliance teams batch-checking vendor lists
- AI agents running a KYC step

## Input

| Field | What it does |
|---|---|
| `names` | **Names to screen**. One per line. |
| `minScore` | **Minimum match score (0-1)**. Similarity threshold. 0.85 is a sensible default. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "names": [
    "Banco Nacional de Cuba",
    "Acme Widgets LLC"
  ],
  "minScore": "0.85",
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "query": "Banco Nacional de Cuba",
  "isPotentialMatch": true,
  "bestScore": 1.0,
  "matches": [
    {
      "score": 1.0,
      "matchedName": "BANCO NACIONAL DE CUBA",
      "sdnName": "BANCO NACIONAL DE CUBA",
      "uid": 306,
      "type": "entity",
      "programs": "CUBA",
      "remarks": "a.k.a. 'BNC'."
    }
  ],
  "listSource": "OFAC SDN + aliases (sanctionslistservice.ofac.treas.gov), fetched at run time"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.003 per screened name** ($3 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://sanctionslistservice.ofac.treas.gov/api/publicationpreview/exports/sdn.csv

Public records only. Nothing is fetched behind a login.

## Limits

- Screens the SDN list only (not the consolidated non-SDN lists). Results are potential matches for human review.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~ofac-sanctions-screening/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"names": ["Banco Nacional de Cuba", "Acme Widgets LLC"], "minScore": "0.85", "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
