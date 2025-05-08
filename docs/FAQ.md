
# FAQ

## DTED Resolution

| Level | SRTM | DTED Post Spacing|Horizontal Accuracy (CE90)|Vertical Accuracy (LE90)|Row x Column|
|---|---|---|---|---|---|
| Level 0  | N/A                  | 30 arc-seconds (900 m) |||121 x 121|
| Level 1  | 3 arc-seconds (~90 m)| 3 arc-seconds (100 m) |50 m|30 m|1200 x 1200|
| Level 2  | 1 arc-second (~30 m) | 1 arc-second (30 m)|23 m|18 m|3600 x 3600|
| Level 3+ | Not applicable       | Higher-res, varies |||||

## What about [my state]?

DTED.org is currently in beta, covering only the state of California. Please contact us (info@snstac.com) to arrange hosting your state's data.

## Will this overwrite my existing DTED data?

ATAK takes an additive approach to unpacking DTED data, that is, it will add new DTED data to existing DTED data. 

For example, if ATAK is configured to use the WA.DTED.org server, and is switched to use the CA.DTED.org server, both states DTED data will persist on the EUD.

## What is the DTED data source?

U.S. President Barack Obama released [Shuttle Radar Topography Mission (SRTM)](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-shuttle-radar-topography-mission-srtm-1) 1 arc-second (SRTM1) derrived DTED2 data on [September 23, 2014](https://www.jpl.nasa.gov/news/us-releases-enhanced-shuttle-land-elevation-data/). [United States Geological Survey (USGS)](https://www.usgs.gov) makes SRTM1 derrived DTED2 data available at [EarthExplore](https://earthexplorer.usgs.gov/).

The [National Geospatial-Intelligence Agency (NGA)](https://www.nga.gov) is an Intelligence Community (IC) & combat support agency responsibile for defining the DTED standard for digital elevation model (DEM) data. DTED follows the specification [MIL-PRF-89020B](http://www.pancroma.com/downloads/MIL-PDF-89020B.pdf) and is available from NGA 

Other DEM specifications, including high [resolution elevation (HRE)](https://www.asprs.org/a/publications/proceedings/sanantonio09/Heady.pdf) data & [USGS GTOPO30](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-global-30-arc-second-elevation-gtopo30), are not yet supported by DTED.org.


## What is the source of the DTED2 data?

There are public, private and restricted sources of DTED2 data. DTED.org hosts SRTM1 derrived DTED2 for the United States, and DTED0 for the rest of the world.

SRTM1 data was colleted between February 11 and 22, 2000 aboard the Space Shuttle Endeavour (STS-99) using the [Shuttle Radar Topography Mission (SRTM)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2005rg000183) mission payload. 

[![SRTM index map](https://dted.org/media/SRTM_2-24-2016-10pct.gif)](https://dted.org/media/SRTM_2-24-2016.gif)

* N.B.: Some restricted DTED data sources (including those from the United States Department of Defense) attempt to model the level of the ground. SRTM attempts to measure the hight of top cover (trees, rooftops, etc). [Source](https://www.civtak.org/elevation-data/)

[![PIA04961: Cape Town, South Africa, Perspective View, Landsat Image over SRTM Elevation](https://dted.org/media/PIA04961_modest-50pct.jpg)](https://dted.org/media/PIA04961_modest.jpg)

## What's the difference between height, elevation & altitude?

Simply put, height is the distance between an object and the ground. Elevation is the distance between mean sea level (MSL) and a point on Earth. Altitude is the distance between a point on Earth and a point in the sky.

DTED provides data on elevation, or the distance between MSL & a point on Earth (for example, the position of an EUD).

[![Height vs Elevation vs Altitude, or "Where does DTED come in?"](https://dted.org/media/elevation-50pct.png)](https://dted.org/media/elevation.png)

## Why can't I use GPS elevation?

The global positioning system (GPS) uses World Geodetic System 1984 (WGS-84) ellipsoid surface as a reference mean sea level (MSL).


## Can't I just use a Data Package?

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

## Under the Hood

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

