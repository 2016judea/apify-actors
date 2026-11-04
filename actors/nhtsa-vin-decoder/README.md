# VIN Decoder (NHTSA vPIC, Batch)

Decode up to thousands of VINs with NHTSA's official vPIC database: make, model, year, trim, body class, engine, displacement, fuel type, drive type, plant, GVWR, safety equipment and error codes. 50 VINs per request.

## Who it's for

- Dealers, auctions and insurers enriching VIN lists
- Fleet and parts businesses
- AI agents answering 'what car is this VIN'

## Input

| Field | What it does |
|---|---|
| `vins` | **VINs**. 17-character VINs, one per line. |
| `maxItems` | **Max results**. Stop after this many results. Each result is one billed event. |

Example input:

```json
{
  "vins": [
    "1HGCM82633A004352",
    "5YJ3E1EA7KF317000"
  ],
  "maxItems": 1000
}
```

## Output

One dataset item per result. A real item from a test run:

```json
{
  "AirBagLocCurtain": "1st and 2nd Rows",
  "AirBagLocFront": "1st Row (Driver and Passenger)",
  "AirBagLocSide": "1st Row (Driver and Passenger)",
  "BedType": "Not Applicable",
  "BodyCabType": "Not Applicable",
  "BodyClass": "Coupe",
  "BusFloorConfigType": "Not Applicable",
  "BusType": "Not Applicable",
  "CustomMotorcycleType": "Not Applicable",
  "DisplacementCC": "2998.832712",
  "DisplacementCI": "183",
  "DisplacementL": "2.998832712",
  "Doors": "2",
  "EngineConfiguration": "V-Shaped",
  "EngineCylinders": "6",
  "EngineHP": "240",
  "EngineModel": "J30A4",
  "ErrorCode": "0",
  "ErrorText": "0 - VIN decoded clean. Check Digit (9th position) is correct",
  "FuelTypePrimary": "Gasoline",
  "GVWR": "Class 1C: 4,001 - 5,000 lb (1,814 - 2,268 kg)",
  "GVWR_to": "Class 1: 6,000 lb or less (2,722 kg or less)",
  "Make": "HONDA",
  "MakeID": "474",
  "Manufacturer": "AMERICAN HONDA MOTOR CO., INC.",
  "ManufacturerId": "988",
  "Model": "Accord",
  "ModelID": "1861",
  "ModelYear": "2003",
  "MotorcycleChassisType": "Not Applicable",
  "MotorcycleSuspensionType": "Not Applicable",
  "OtherRestraintSystemInfo": "Seat Belt (Rr center position)",
  "PlantCity": "MARYSVILLE",
  "PlantCountry": "UNITED STATES (USA)",
  "PlantState": "OHIO",
  "SeatBeltsAll": "Manual",
  "TrailerBodyType": "Not Applicable",
  "TrailerType": "Not Applicable",
  "TransmissionSpeeds": "5",
  "TransmissionStyle": "Automatic",
  "Trim": "EX-V6",
  "VIN": "1HGCM82633A004352",
  "ValveTrainDesign": "Single Overhead Cam (SOHC)",
  "VehicleDescriptor": "1HGCM826*3A",
  "VehicleType": "PASSENGER CAR"
}
```

Download as JSON, CSV, Excel or via the Apify API.

## Pricing

Pay per result: **$0.002 per decoded vin** ($2 per 1,000). No monthly fee. Set a max charge on the run and it stops there. AI agents can run it with agentic payments where Apify enables them.

## Data source

Fetched live at run time from the public source: https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/

Public records only. Nothing is fetched behind a login.

## Use it from code or an AI agent

```bash
curl -X POST 'https://api.apify.com/v2/acts/cheerful_term~nhtsa-vin-decoder/run-sync-get-dataset-items?token=YOUR_TOKEN' \
  -H 'Content-Type: application/json' -d '{"vins": ["1HGCM82633A004352", "5YJ3E1EA7KF317000"], "maxItems": 1000}'
```

Part of a set of public-records actors by cheerful_term: https://apify.com/cheerful_term
