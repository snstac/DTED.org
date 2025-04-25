![DTED.org Logo](media/noun-elevation-5901019-10pct.png)

# DTED.org: Digital Terrain Elevation Data Enclave for TAK

DTED.org is a specialized hosting service providing [digital terrain elevation data (DTED)](https://en.wikipedia.org/wiki/DTED) for use with the [Team Awareness Kit (TAK)](https://www.tak.gov) suite of products. The service enhances mapping capabilities by delivering higher-resolution elevation data than standard options.

---

## Why Elevation Data Matters

The accuracy and detail of elevation data are directly related to DTED resolution—higher resolution provides better data quality. Precise elevation information is essential for:

- Line-of-sight analyses
- Terrain visualization
- Mission planning
- Navigation tasks
- Tactical operations

---

## Technical Specifications

DTED follows the specification [**MIL-PRF-89020B**](http://www.pancroma.com/downloads/MIL-PDF-89020B.pdf) standard.

---

## Integration Options

DTED.org offers two integration methods with ATAK:

1. **DTED Stream Server**
   Functions as a drop-in replacement for ATAK's default DTED Stream Server (TPC). Works with off-the-shelf ATAK, no additional plugins required.

2. **Simple DTED Streamer**  
   Operates as a Simple DTED Server for ATAK's [Simple DTED Streamer](https://tak.gov/plugins/simple-dted-streamer) plugin.

---

## Comparison with TPC DTED Stream Server

ATAK's default DTED data source is the TPC's DTED Stream Server at TAK.gov, which provides DTED0 files according to ATAK documentation:

> TPC provides DTED0 for four corners of the hemisphere via downloadable .zip files that contain uncompressed DTED files.

The "Four Corners" refer to the Earth's hemispheres:  

- **North West (NW)** (includes CONUS)  
- **North East (NE)**  
- **South West (SW)**  
- **South East (SE)**  

---

## DTED.org's Enhanced Approach

For each U.S. state, DTED.org adds DTED2 data to the four corners DTED file for that hemisphere. Benefits include:

- Download hemisphere-level DTED0 data from alternative sources.
- Simultaneously obtain state-level DTED2 data for an area of interest (AOI).
- Complete the entire process in a single request.
- Integrate data without manual loading (no hand jamming).
- Enable setup through a simple QR code scan.

---

## Performance Improvement

Once implemented on an ATAK end-user device, elevation accuracy can improve to approximately **30 meters** — significantly better than standard DTED0 resolution.

---

## How to Use DTED.org

### 1. Automatically with a QR Code

Scan the following QR code using the camera on your ATAK device (use the Android camera app, not ATAK QuickCam):

![ATAK DTED QR code for California](https://CA.DTED.org/CA-QR.png)

### 2. Manually via ATAK

[TK]

### 3. Using an ATAK Preferences File

Add the following entries to your ATAK preferences file:

```xml
<entry key="prefs_dted_stream_server" class="class java.lang.String">CA.DTED.org</entry>
<entry key="simpleDtedStreamer.streaming_dted_uri_key" class="class java.lang.String">https://CA.DTED.org</entry>
<entry key="prefs_dted_stream" class="class java.lang.Boolean">true</entry>
```

[Sample ATAK preferences file](https://ca.dted.org/CA.DTED.org.pref).

---

## Other TAK Tools

For California **(explicit values for ATAK)**:
* DTED Stream Server: `ca.dted.org`
* Simple DTED Server: `https://ca.dted.org`

---

## FAQ

### Will this overwrite my existing DTED data?

ATAK takes an additive approach to unpacking DTED data, that is, it will add new DTED data to existing DTED data. 

For example, if ATAK is configured to use the WA.DTED.org server, and is switched to use the CA.DTED.org server, both states DTED data will persist on the EUD.

### Can't I just use a Data Package?

If managing Data Packages is your thing, by all means.

---

### Under the Hood

### ATAK Off-the-Shelf

For each state, DTED.org creates an enhanced NW hemisphere DTED data file. The enhanced file contains both DTED0 data as well as DTED2 data for that state.

For example:

> The TPC four-corners DTED file for NW contains this area of California at DTED0 (900 m) resolution:
>* `w115/n32.dt0`
>
> DTED creates a unique state-by-state four-corners DTED file for NW containing the file:
>* `w115/n32.dt2`
>
> This adds DTED2 (30 m) for that area of California.

---

### Simple DTED Server

Provides and index and compressed DTED files for each state through normal plugin configuration using a state-by-state URL with the following schema:

* Server Name: `https://STATE.dted.org`
	* Where `STATE` is your state's two letter abbreviation. 
	  For Example: For California (`CA`) Server Name: `https://CA.dted.org`

---

### DTED Resolution

| Level    | SRTM                 | DTED                                                    |
| -------- | -------------------- | ------------------------------------------------------- |
| Level 0  | N/A                  | 30 arc-second (~1 km)                                   |
| Level 1  | 3 arc-second (~90 m) | 3 arc-second (~90 m)                                    |
| Level 2  | 1 arc-second (~30 m) | 1 arc-second (~30 m)                                    |
| Level 3+ | Not applicable       | Higher-res, varies (classified or limited availability) |
