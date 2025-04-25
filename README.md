![](https://dted.org/media/DTED.org-50pct.png)

# DTED.org: Digital Terrain Elevation Data Enclave for TAK

[DTED.org](https://dted.org) is a specialized hosting service providing [digital terrain elevation data (DTED)](https://en.wikipedia.org/wiki/DTED) for use with the [Team Awareness Kit (TAK)](https://www.tak.gov) suite of products. The service enhances mapping capabilities by delivering higher-resolution elevation data to TAK end user devices (EUDs), including Android Team Awareness Kit (ATAK).

---

## Why Elevation Data Matters

The accuracy and detail of elevation data are directly related to DTED resolution—higher resolution provides better data quality. Precise elevation information is essential for:

- Line-of-sight analyses
- Terrain visualization
- Mission planning
- Navigation tasks
- Tactical operations
- Disaster response operations

---

## Integration Options

DTED.org offers two integration methods with ATAK:

1. **DTED Stream Server**

   Functions as a drop-in replacement for ATAK's default DTED Stream Server (TPC). Works with off-the-shelf ATAK, no additional plugins required.

2. **Simple DTED Streamer**

   Operates as a Simple DTED Server for ATAK's [Simple DTED Streamer](https://tak.gov/plugins/simple-dted-streamer) plugin.

---

## Comparison with TPC DTED Stream Server

ATAK's default DTED data source is the TPC's DTED Stream Server at TAK.gov, which provides DTED0 (90 m/295 ft) files:

> "TPC provides DTED0 for four corners of the hemisphere via downloadable .zip files that contain uncompressed DTED files." 
> [Source: tak.gov](https://tak.gov)

The "Four Corners" refer to the Earth's hemispheres:  

- **North West (NW)** (includes CONUS)  
- **North East (NE)**  
- **South West (SW)**  
- **South East (SE)**  

---

## DTED.org's Enhanced Approach

For each U.S. state, DTED.org adds DTED2 (30 m/98 ft) data to the four corners DTED file for that hemisphere. Benefits include:

- Download hemisphere-level DTED0 data from alternative sources.
- Simultaneously obtain state-level DTED2 data for an area of interest (AOI).
- Complete the entire process in a single request.
- Integrate data without manual loading (no hand jamming).
- Enable setup through a simple QR code scan.

---

## Performance Improvement

Once implemented on an ATAK end-user device, elevation accuracy can improve to approximately **30 meters/98 feet** — significantly better than standard DTED0 resolution.

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

* DTED Stream Server: `CA.DTED.org`

* Simple DTED Server: `https://CA.DTED.org`

---

## FAQ

### What about [my state]?

DTED.org is currently in beta, covering only the state of California. Please contact us (info@snstac.com) to arrange hosting your state's data.

### Will this overwrite my existing DTED data?

ATAK takes an additive approach to unpacking DTED data, that is, it will add new DTED data to existing DTED data. 

For example, if ATAK is configured to use the WA.DTED.org server, and is switched to use the CA.DTED.org server, both states DTED data will persist on the EUD.

### Isn't DTED2 data restricted.

U.S. President Barack Obama released SRTM1 derrived DTED2 data on [September 23, 2014](https://www.jpl.nasa.gov/news/us-releases-enhanced-shuttle-land-elevation-data/).

USGS makes DTED2 data available at [EarthExplore](https://earthexplorer.usgs.gov/).

### What is the source of the DTED2 data?

There are public, private and restricted sources of DTED2 data. DTED.org hosts SRTM1 derrived DTED2 for the United States, and DTED0 for the rest of the world.

SRTM1 data was colleted between February 11 and 22, 2000 aboard the Space Shuttle Endeavour (STS-99) using the [Shuttle Radar Topography Mission (SRTM)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2005rg000183) mission payload. 

[![SRTM index map](https://dted.org/media/SRTM_2-24-2016-10pct.gif)](https://dted.org/media/SRTM_2-24-2016.gif)

* N.B.: Some restricted DTED data sources (including those from the United States Department of Defense) attempt to model the level of the ground. SRTM attempts to measure the hight of top cover (trees, rooftops, etc). [Source](https://www.civtak.org/elevation-data/)


### Can't I just use a Data Package?

Sure, here's a couple of alternative guides to utilizing DTED data within ATAK:

* [DTED2 Instructional for TAK using USGS EarthExplorer](https://www.youtube.com/watch?v=Z0DCMBjYwi4) (via Marshall Frith)
* [Downloading SRTM DTED2 elevation models from USGS](https://www.reddit.com/r/ATAK/comments/hjtlki/downloading_srtm_dted2_elevation_models_from_usgs/) (via field_mapper)
* [Loading DTED in ATAK](https://www.youtube.com/watch?v=1pgaGbGBZb8) (via Tough Stump Technologies)
* [ATAK for Hikers](https://paul-mandal.medium.com/atak-for-hikers-d96d5246193e) (via Paul Mandal)
* [Disseminating Remotely Sensed Products using ATAK](https://fsapps.nwcg.gov/nirops/docs/upload/11b_Redacted_ATAK_TFRSAC_Presentation.pdf) (via Colorado CoE)
* [ATAK DTED DP Downloader](https://github.com/rick51231/atak-dted-dp-downloader/) (via Rick)
* [ATAK-Civ Tutorial B13: Elevation Tool](https://www.youtube.com/watch?v=g1wwj2q7Sgo) (via ATAKwizard)

[CivTAK.org](https://www.civtak.org/) guides:

* [Downloading SRTM for TAK](https://www.civtak.org/2020/04/19/downoading-srtm-for-tak/)
* [How to Download SRTM Data for use in ATAK/WinTAK/WebTAK](https://www.youtube.com/watch?v=Hm8yk4rN86k)
* [Importing zipped SRTM/DTED into ATAK](https://www.youtube.com/watch?v=UvDtNTvqK2E)
* [How to Tell SRTM Has Been Properly Imported into ATAK](https://www.youtube.com/watch?v=H2fYRnqu-T0)
* [ATAK Tutorial -- Elevation Heatmap, Red X, SRTM/DTED Import](https://www.youtube.com/watch?v=vrBW-VGCbxo)
* [Civilian DTED](https://www.civtak.org/files/)

### DTED Resolution

| Level    | SRTM                 | DTED                                                    |
| -------- | -------------------- | ------------------------------------------------------- |
| Level 0  | N/A                  | 30 arc-second (~1 km)                                   |
| Level 1  | 3 arc-second (~90 m) | 3 arc-second (~90 m)                                    |
| Level 2  | 1 arc-second (~30 m) | 1 arc-second (~30 m)                                    |
| Level 3+ | Not applicable       | Higher-res, varies (classified or limited availability) |

### Technical Specifications

DTED follows the specification [**MIL-PRF-89020B**](http://www.pancroma.com/downloads/MIL-PDF-89020B.pdf) standard.

---

### Under the Hood

### ATAK Off-the-Shelf

For each state, DTED.org creates an enhanced NW hemisphere DTED data file. The enhanced file contains both DTED0 data as well as DTED2 data for that state.

For example:

> The TPC four-corners DTED file for NW contains this area of California at DTED0 (900 m) resolution:
>
> * `w115/n32.dt0`
>
> DTED creates a unique state-by-state four-corners DTED file for NW containing the file:
>
> * `w115/n32.dt2`
>
> This adds DTED2 (30 m) for that area of California.

### Simple DTED Server

Provides and index and compressed DTED files for each state through normal plugin configuration using a state-by-state URL with the following schema:

* Server Name: `https://STATE.DTED.org`
	* Where `STATE` is your state's two letter abbreviation. 
	  For Example: For California (`CA`) Server Name: `https://CA.DTED.org`

--- 

## License, Copyright and Contact

* Contact: [info@snstac.com](mailto:info@snstac.com)
* Source code for DTED.org is available at [GitHub](https://github.com/snstac/DTED.org)


Copyright Sensors & Signals LLC https://www.snstac.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
