FIELDS = ("id,title,agency,awardeeName,awardeeCity,awardeeStateCode,fundsObligatedAmt,estimatedTotalAmt,startDate,expDate,"
          "piFirstName,piLastName,poName,fundProgramName,abstractText,date,primaryProgram,transType")


async def run(inp, client, emit):
    params = {"printFields": FIELDS, "rpp": 25, "offset": 1}
    if inp.get("keyword"):
        params["keyword"] = inp["keyword"]
    if inp.get("awardeeState"):
        params["awardeeStateCode"] = inp["awardeeState"].upper()
    if inp.get("awardee"):
        params["awardeeName"] = inp["awardee"]
    if inp.get("startDateFrom"):
        y, m, d = inp["startDateFrom"].split("-")
        params["startDateStart"] = f"{m}/{d}/{y}"
    while params["offset"] < 3000:
        d = await client.json("https://api.nsf.gov/services/v1/awards.json", params=params)
        aw = d.get("response", {}).get("award", [])
        for a in aw:
            a["url"] = f"https://www.nsf.gov/awardsearch/showAward?AWD_ID={a.get('id')}"
            await emit(a)
        if len(aw) < 25:
            return
        params["offset"] += 25
