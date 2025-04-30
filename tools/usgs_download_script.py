#!/usr/bin/env python3
"""
USGS M2M API Script for Downloading DTED/SRTM Data by State
This script allows you to download Digital Terrain Elevation Data (DTED) and
Shuttle Radar Topography Mission (SRTM) data for a specified US state.
"""
import os
import json
import time
import requests
import argparse
from shapely.geometry import shape
import us


def get_api_key():
    """Get USGS API key from environment or prompt user."""
    api_key = os.environ.get("USGS_API_KEY")
    if not api_key:
        api_key = input("Enter your USGS API key: ")
    return api_key


def get_usgs_token(api_url, username, password):
    """Authenticate with USGS M2M API and get token."""
    payload = {"username": username, "token": password}
    response = requests.post(f"{api_url}/login-token", json=payload)
    response.raise_for_status()
    return response.json()["data"]


def search_datasets(api_url, token, dataset_names=None):
    """Search for specific datasets or list all available datasets."""
    headers = {"X-Auth-Token": token}
    response = requests.get(f"{api_url}/dataset-search", headers=headers)
    response.raise_for_status()
    datasets = response.json()["data"]

    if dataset_names:
        return [ds for ds in datasets if ds["datasetAlias"] in dataset_names]
    return datasets


def get_state_boundary(state_name):
    """Get state boundary geometry."""
    # Convert state name to state object
    state = us.states.lookup(state_name)
    if not state:
        raise ValueError(f"Invalid state name: {state_name}")

    # Use the Census API to get state boundaries
    url = f"https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/MapServer/0/query"
    params = {
        "where": f"NAME='{state.name}'",
        "outFields": "*",
        "geometryPrecision": 6,
        "outSR": 4326,
        "f": "geojson",
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    geojson = response.json()

    if not geojson["features"]:
        raise ValueError(f"Could not find boundary for state: {state.name}")

    return geojson["features"][0]["geometry"]


def search_scenes(api_url, token, dataset_id, state_geometry):
    """Search for scenes covering the state."""
    headers = {"X-Auth-Token": token}
    payload = {
        "datasetName": dataset_id,
        "spatialFilter": {"filterType": "geojson", "geoJson": state_geometry},
        "maxResults": 50000,  # Adjust as needed
    }

    response = requests.post(f"{api_url}/scene-search", json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["data"]["results"]


def download_scenes(api_url, token, dataset_id, scene_ids, download_dir):
    """Request download URLs for selected scenes and download them."""
    headers = {"X-Auth-Token": token}

    # Create the download directory if it doesn't exist
    os.makedirs(download_dir, exist_ok=True)

    # Request download URLs
    payload = {"datasetName": dataset_id, "entityIds": scene_ids}

    print(f"Requesting download URLs for {len(scene_ids)} scenes...")
    print(f"{api_url}/download-request")
    print(payload)
    print(headers)
    response = requests.post(
        f"{api_url}/download-request", json=payload, headers=headers
    )
    response.raise_for_status()

    # Get the download ID
    download_id = response.json()["data"]["downloadId"]

    # Check download status until ready
    download_ready = False
    print("Waiting for download preparation...")
    while not download_ready:
        status_response = requests.get(
            f"{api_url}/download-retrieve/{download_id}", headers=headers
        )
        status_response.raise_for_status()
        status_data = status_response.json()["data"]

        if status_data["status"] == "available":
            download_ready = True
        elif status_data["status"] == "failed":
            print("Download preparation failed")
            return
        else:
            print(f"Download status: {status_data['status']}, waiting 10 seconds...")
            time.sleep(10)

    # Get download URLs
    print("Download ready, retrieving URLs...")
    download_response = requests.get(
        f"{api_url}/download-retrieve/{download_id}", headers=headers
    )
    download_response.raise_for_status()
    download_urls = download_response.json()["data"]["availableDownloads"]

    # Download files
    print(f"Starting download of {len(download_urls)} files to {download_dir}")
    for i, download_item in enumerate(download_urls):
        url = download_item["url"]
        filename = os.path.basename(url.split("?")[0])
        filepath = os.path.join(download_dir, filename)

        print(f"Downloading file {i+1}/{len(download_urls)}: {filename}")
        file_response = requests.get(url, stream=True)
        file_response.raise_for_status()

        with open(filepath, "wb") as f:
            for chunk in file_response.iter_content(chunk_size=8192):
                f.write(chunk)

    print(f"Download completed: {len(download_urls)} files saved to {download_dir}")


def main():
    """Main function to orchestrate the DTED/SRTM data download."""
    parser = argparse.ArgumentParser(
        description="Download DTED/SRTM data for a US state using USGS M2M API"
    )
    parser.add_argument("state", help="US state name")
    parser.add_argument("--username", help="USGS EarthExplorer username")
    parser.add_argument("--password", help="USGS EarthExplorer password")
    parser.add_argument(
        "--dataset", default="all", help="Dataset to download (srtm, dted, or all)"
    )
    parser.add_argument(
        "--output",
        default="./usgs_elevation_data",
        help="Output directory for downloaded files",
    )
    args = parser.parse_args()

    # USGS M2M API URL
    api_url = "https://m2m.cr.usgs.gov/api/api/json/stable"

    # Get credentials
    username = args.username or input("Enter your USGS EarthExplorer username: ")
    password = args.password or input("Enter your USGS EarthExplorer password: ")

    # Get state boundary
    try:
        print(f"Getting boundary for state: {args.state}")
        state_geometry = get_state_boundary(args.state)
    except Exception as e:
        print(f"Error getting state boundary: {e}")
        return

    # Map dataset input to actual dataset aliases
    dataset_aliases = []
    if args.dataset.lower() == "all" or args.dataset.lower() == "srtm":
        dataset_aliases.extend(["SRTM 1 Arc-Second Global", "SRTM 3 Arc-Second Global"])
    if args.dataset.lower() == "all" or args.dataset.lower() == "dted":
        dataset_aliases.extend(["DTED Level 0", "DTED Level 1", "DTED Level 2"])

    try:
        # Get authentication token
        print("Authenticating with USGS M2M API...")
        token = get_usgs_token(api_url, username, password)
        print("Authentication successful")

        # Get dataset information
        print("Searching for datasets...")
        datasets = search_datasets(api_url, token, dataset_aliases)

        if not datasets:
            print(f"No datasets found matching: {dataset_aliases}")
            return

        # Process each dataset
        for dataset in datasets:
            dataset_id = dataset["datasetAlias"]
            print(f"\nProcessing dataset: {dataset_id}")

            # Create dataset-specific output directory
            dataset_output_dir = os.path.join(args.output, dataset_id.replace(" ", "_"))

            # Search for scenes
            print(f"Searching for scenes in {args.state}...")
            scenes = search_scenes(api_url, token, dataset_id, state_geometry)

            if not scenes:
                print(f"No scenes found for {dataset_id} in {args.state}")
                continue

            print(f"Found {len(scenes)} scenes")

            # Get scene IDs
            scene_ids = [scene["entityId"] for scene in scenes]

            # Download scenes
            download_scenes(api_url, token, dataset_id, scene_ids, dataset_output_dir)

    except Exception as e:
        print(f"Error: {e}")

    print("Script execution completed")


if __name__ == "__main__":
    main()
