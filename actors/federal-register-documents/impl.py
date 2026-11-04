FIELDS = ["document_number", "title", "type", "abstract", "publication_date", "effective_on", "comments_close_on",
          "agencies", "html_url", "pdf_url", "docket_ids", "regulation_id_numbers", "significant", "cfr_references", "action"]


async def run(inp, client, emit):
    params = [("per_page", 100), ("order", "newest")] + [("fields[]", f) for f in FIELDS]
    if inp.get("query"):
        params.append(("conditions[term]", inp["query"]))
    for t in inp.get("types") or []:
        params.append(("conditions[type][]", t))
    if inp.get("agency"):
        params.append(("conditions[agencies][]", inp["agency"]))
    if inp.get("publishedSince"):
        params.append(("conditions[publication_date][gte]", inp["publishedSince"]))
    if inp.get("openForComment"):
        params.append(("conditions[comment_date][gte]", __import__("datetime").date.today().isoformat()))
    url = "https://www.federalregister.gov/api/v1/documents.json"
    page = 1
    while True:
        d = await client.json(url, params=params + [("page", page)])
        for r in d.get("results", []):
            r["agencies"] = [a.get("name") for a in r.get("agencies") or []]
            r["cfr_references"] = [f'{c.get("title")} CFR {c.get("part")}' for c in r.get("cfr_references") or []]
            await emit(r)
        if not d.get("next_page_url") or page >= 100:
            return
        page += 1
