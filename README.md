![](https://dted.readthedocs.io/en/latest/media/noun-elevation-5901019-10pct.png)

# DTED.org: Digital Terrain Elevation Data Enclave for TAK

[DTED.org](https://dted.org) is a dedicated service for hosting [Digital Terrain Elevation Data (DTED)](https://en.wikipedia.org/wiki/DTED), optimized for the [Team Awareness Kit (TAK)](https://www.tak.gov) ecosystem. By providing high-resolution elevation datasets, DTED.org enhances mapping and situational awareness for TAK end-user devices (EUDs), including Android Team Awareness Kit (ATAK) and WinTAK.

Integrating DTED.org with TAK EUDs enables elevation accuracy up to **30 meters (98 feet)**, a substantial improvement over the standard DTED0 resolution of 300 meters (900 feet).

Documentation is available at [docs.DTED.org](https://docs.DTED.org/)

---

## Why Elevation Data Matters

[![Notional Difference in DTED Resolution](https://dted.readthedocs.io/en/latest/media/dted_resolution-10pct.png)](https://dted.readthedocs.io/en/latest/media/dted_resolution.png)

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

For each U.S. state, DTED.org seamlessly overlays high-resolution DTED2 (30 m/98 ft) data onto standard DTED0 (300 m/900 ft) coverage. Key advantages:

- Instantly access state-level DTED2 data for any area of interest (AOI).
- Download broader hemisphere-level DTED0 data from alternative sources as needed.
- Complete data acquisition and integration in a single streamlined request.
- Eliminate manual data loading. No hand-jamming required!
- Simplify device setup with a quick QR code scan.


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
