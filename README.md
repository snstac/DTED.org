![](https://dted.org/media/noun-elevation-5901019-10pct.png)

# DTED.org: Digital Terrain Elevation Data Enclave for TAK

[DTED.org](https://dted.org) is a specialized hosting service providing [digital terrain elevation data (DTED)](https://en.wikipedia.org/wiki/DTED) for use with the [Team Awareness Kit (TAK)](https://www.tak.gov) suite of products. The service enhances mapping capabilities by delivering higher-resolution elevation data to TAK end user devices (EUDs), including Android Team Awareness Kit (ATAK).

Once implemented on an TAK end-user device, elevation accuracy can improve to approximately **30 meters/98 feet** — significantly better than standard DTED0 (300 meters/900 feet) resolution.

Documentation is available at [docs.DTED.org](https://docs.DTED.org/)

---

## Why Elevation Data Matters

[![Notional Difference in DTED Resolution](https://dted.org/media/dted_resolution-10pct.png)](https://dted.org/media/dted_resolution.png)

The accuracy and quality of elevation data depend on the resolution of the DTED and the reference used for mean sea level (zero elevation). Higher resolution provides more detailed and precise elevation data, which is essential for various applications, such as:

* Flight operations for crewed and uncrewed systems (e.g., UAS, drones)
* Line-of-sight analysis
* Terrain visualization
* Mission planning
* Navigation
* Tactical operations
* Disaster response efforts

DTED uses the Earth Gravitational Model 1996 (EGM96) geoid model as its zero elevation reference, while GPS relies on the World Geodetic System 1984 (WGS-84) ellipsoid model. These two models can differ significantly, often requiring geoid corrections to align GPS elevations with actual ground elevations. However, DTED-derived elevation data does not require such corrections.


---

## DTED.org's Enhanced Approach

For each U.S. state, DTED.org adds DTED2 (30 m/98 ft) data to existing DTED0 (300 m/900 ft) data. Benefits include:

- Download hemisphere-level DTED0 data from alternative sources.
- Simultaneously obtain state-level DTED2 data for an area of interest (AOI).
- Complete the entire process in a single request.
- Integrate data without manual loading (no hand jamming!).
- Enable setup through a simple QR code scan.

---

## License, Copyright and Contact

* Contact: [info@snstac.com](mailto:info@snstac.com)
* Source code for DTED.org is available at [GitHub](https://github.com/snstac/DTED.org)


Copyright Sensors & Signals LLC [https://www.snstac.com](https://www.snstac.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
