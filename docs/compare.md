# DTED Comparison

## DTED Resolution

| Level | SRTM | DTED Post Spacing|Horizontal Accuracy (CE90)|Vertical Accuracy (LE90)|Row x Column|
|---|---|---|---|---|---|
| Level 0  | N/A                  | 30 arc-seconds (900 m) |||121 x 121|
| Level 1  | 3 arc-seconds (~90 m)| 3 arc-seconds (100 m) |50 m|30 m|1200 x 1200|
| Level 2  | 1 arc-second (~30 m) | 1 arc-second (30 m)|23 m|18 m|3600 x 3600|
| Level 3+ | Not applicable       | Higher-res, varies |||||

## Comparison with TPC DTED Stream Server

ATAK's default DTED data source is the TPC's DTED Stream Server at TAK.gov, which provides DTED0 (90 m/295 ft) files:

> "TPC provides DTED0 for four corners of the hemisphere via downloadable .zip files that contain uncompressed DTED files." 
> [Source: tak.gov](https://tak.gov)

The "Four Corners" refer to the Earth's hemispheres:  

- **North West (NW)** (includes CONUS)  
- **North East (NE)**  
- **South West (SW)**  
- **South East (SE)**  
