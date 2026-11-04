async def run(inp, client, emit):
    params = {"format": "json"}
    if inp.get("recalledSince"):
        params["RecallDateStart"] = inp["recalledSince"]
    if inp.get("keyword"):
        params["ProductName"] = inp["keyword"]
    if inp.get("manufacturer"):
        params["Manufacturer"] = inp["manufacturer"]
    d = await client.json("https://www.saferproducts.gov/RestWebServices/Recall", params=params)
    d = sorted(d, key=lambda r: r.get("RecallDate") or "", reverse=True)
    for r in d:
        def names(k, f="Name"):
            return [x.get(f) for x in (r.get(k) or []) if x.get(f)]
        await emit({
            "recallNumber": r.get("RecallNumber"), "recallDate": (r.get("RecallDate") or "")[:10], "title": r.get("Title"),
            "description": r.get("Description"), "url": r.get("URL"), "products": names("Products"),
            "units": [x.get("NumberOfUnits") for x in r.get("Products") or [] if x.get("NumberOfUnits")],
            "hazards": names("Hazards"), "remedies": names("Remedies"), "remedyOptions": names("RemedyOptions", "Option"),
            "manufacturers": names("Manufacturers"), "retailers": names("Retailers"), "importers": names("Importers"),
            "distributors": names("Distributors"), "manufacturerCountries": names("ManufacturerCountries", "Country"),
            "injuries": names("Injuries"), "consumerContact": r.get("ConsumerContact"),
            "images": [x.get("URL") for x in r.get("Images") or []], "lastPublishDate": (r.get("LastPublishDate") or "")[:10],
        })
