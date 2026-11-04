# Federal Register: Rules, Notices & Comment Deadlines

Search the daily Federal Register: proposed rules, final rules, notices and presidential documents with agency, abstract, publication, effective and comment-close dates, docket and RIN, CFR parts and links. Filter by term, type, agency, date or open-for-comment.

## Who it's for

- Compliance and regulatory teams watching rules in their industry
- Trade associations tracking comment deadlines
- AI agents answering 'what changed this week for X'

## Input

| Field | What it does |
|---|---|
| `query` | **Search term**. Full-text term, e.g. PFAS |
| `types` | **Document types**. RULE, PRORULE, NOTICE, PRESDOCU |
| `agency` | **Agency slug**. e.g. environmental-protection-agency |
| `publishedSince` | **Published on or after (YYYY-MM-DD)**. Only documents published on or after this date. |
| `openForComment` | **Open for comment only**. Comment period has not closed. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "query": "PFAS",
  "types": [
    "RULE",
    "PRORULE"
  ],
  "publishedSince": "2026-01-01",
  "openForComment": false,
  "maxItems": 100
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "document_number": "2026-21669",
  "title": "Hazard Analysis and Risk-Based Preventive Controls for Human Food; Draft Guidance for Industry; Availability",
  "type": "Proposed Rule",
  "abstract": "The Food and Drug Administration (FDA, the Agency, or we) is announcing the availability of one additional draft chapter of a multichapter draft guidance for industry titled \"Hazard Analysis and Risk-Based Preventive Controls for Human Food.\" This multichapter draft guidance, when finalized, will explain FDA's current thinking on how to comply with the requirements for hazard analysis and risk-based preventive controls under FDA's regulation titled \"Current Good Manufacturing Practice, Hazard Analysis, and Risk-Based Preventive Controls for Human Food.\" The newly available draft chapter is titled \"Chapter 12: Control of Chemical Hazards.\" This draft guidance is not final nor is it in effect at this time.",
  "publication_date": "2026-10-23",
  "effective_on": null,
  "comments_close_on": "2027-01-21",
  "agencies": [
    "Health and Human Services Department",
    "Food and Drug Administration"
  ],
  "html_url": "https://www.federalregister.gov/documents/2026/10/23/2026-21669/hazard-analysis-and-risk-based-preventive-controls-for-human-food-draft-guidance-for-industry",
  "pdf_url": "https://www.govinfo.gov/content/pkg/FR-2026-10-23/pdf/2026-21669.pdf",
  "docket_ids": [
    "Docket No. FDA-2016-D-2343"
  ],
  "regulation_id_numbers": [],
  "significant": null,
  "cfr_references": [
    "21 CFR 117"
  ],
  "action": "Notification of availability."
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per document** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://www.federalregister.gov/api/v1/documents.json

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~federal-register-documents/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"query": "PFAS", "types": ["RULE", "PRORULE"], "publishedSince": "2026-01-01", "openForComment": false, "maxItems": 100}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
