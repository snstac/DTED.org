#!/usr/bin/env python3
"""
dted-coverage-visualizer.py

Visualize DTED data coverage from a directory structure.
This script scans a directory for DTED files, extracts coverage information,
and generates a map showing the coverage of different DTED levels.

Usage:

    python dted-coverage-visualizer.py <directory> [options]

Options:
    -h, --help            Show this help message and exit
    -o, --output <file>   Output file path (e.g., coverage_map.png)
    --no-grid             Disable grid lines
    -r, --region <region> Filter by region (N=North, S=South, E=East, W=West,
                            or combinations for quadrants)
                            (e.g., NW, NE, SW, SE)
"""


import os
import re
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import argparse
from matplotlib.ticker import MultipleLocator
import math

# Set up matplotlib to use a non-interactive backend
plt.switch_backend("Agg")  # Use 'Agg' for non-interactive backends
# Define a custom colormap for DTED levels
cmap = LinearSegmentedColormap.from_list(
    "dted_cmap", ["yellow", "green", "blue"], N=256
)

# Set the default font size for matplotlib
plt.rcParams["font.size"] = 12
# Set the default figure size for matplotlib
plt.rcParams["figure.figsize"] = (12, 8)
# Set the default figure dpi for matplotlib
plt.rcParams["figure.dpi"] = 300
# Set the default line width for matplotlib
plt.rcParams["lines.linewidth"] = 1.5
# Set the default grid color for matplotlib
plt.rcParams["grid.color"] = "gray"
# Set the default grid linestyle for matplotlib
plt.rcParams["grid.linestyle"] = "--"
# Set the default grid linewidth for matplotlib
plt.rcParams["grid.linewidth"] = 0.5
# Set the default grid alpha for matplotlib
plt.rcParams["grid.alpha"] = 0.7
# Set the default legend font size for matplotlib
plt.rcParams["legend.fontsize"] = 10
# Set the default legend loc for matplotlib
plt.rcParams["legend.loc"] = "upper right"
# Set the default legend frameon for matplotlib
plt.rcParams["legend.frameon"] = True
# Set the default legend shadow for matplotlib
plt.rcParams["legend.shadow"] = True

# Set the default legend fancybox for matplotlib
plt.rcParams["legend.fancybox"] = True
# Set the default legend borderpad for matplotlib
plt.rcParams["legend.borderpad"] = 0.5
# Set the default legend borderaxespad for matplotlib
plt.rcParams["legend.borderaxespad"] = 0.5
# Set the default legend handlelength for matplotlib
plt.rcParams["legend.handlelength"] = 1.5
# Set the default legend handletextpad for matplotlib
plt.rcParams["legend.handletextpad"] = 0.5
# Set the default legend markerscale for matplotlib
plt.rcParams["legend.markerscale"] = 1.0
# Set the default legend title_fontsize for matplotlib
plt.rcParams["legend.title_fontsize"] = 12
# Set the default legend title for matplotlib
plt.rcParams["legend.title"] = "DTED Levels"


def parse_dted_path(path):
    """Extract longitude, latitude, and DTED level from a path."""
    # Define regex patterns for extraction
    lon_pattern = r"([ew])(\d+)"  # e.g., 'w115'
    lat_pattern = r"([ns])(\d+)"  # e.g., 'n32'
    level_pattern = r"dt(\d+)"  # e.g., 'dt2'

    # Find all matches
    lon_match = re.search(lon_pattern, path.lower())
    lat_match = re.search(lat_pattern, path.lower())
    level_match = re.search(level_pattern, path.lower())

    if not (lon_match and lat_match and level_match):
        return None

    # Extract values
    lon_dir, lon_val = lon_match.groups()
    lat_dir, lat_val = lat_match.groups()
    level = level_match.group(1)

    # Convert to numeric values
    lon = int(lon_val)
    if lon_dir == "w":
        lon = -lon  # West is negative

    lat = int(lat_val)
    if lat_dir == "s":
        lat = -lat  # South is negative

    return lon, lat, int(level)


def scan_directory(root_dir):
    """Scan directory for DTED files and extract coverage information."""
    coverage = {}  # Dictionary to store coverage by level

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if (
                file.lower().endswith(".dt0")
                or file.lower().endswith(".dt1")
                or file.lower().endswith(".dt2")
            ):
                path = os.path.join(root, file)
                result = parse_dted_path(path)

                if result:
                    lon, lat, level = result
                    if level not in coverage:
                        coverage[level] = set()
                    coverage[level].add((lon, lat))

    return coverage


def filter_by_region(coverage, region=None):
    """Filter coverage data by hemisphere or quadrant."""
    if not region:
        return coverage

    filtered_coverage = {}

    for level, points in coverage.items():
        filtered_points = set()

        for lon, lat in points:
            # Basic hemispheres
            if region.upper() == "N" and lat >= 0:
                filtered_points.add((lon, lat))
            elif region.upper() == "S" and lat < 0:
                filtered_points.add((lon, lat))
            elif region.upper() == "E" and lon >= 0:
                filtered_points.add((lon, lat))
            elif region.upper() == "W" and lon < 0:
                filtered_points.add((lon, lat))
            # Quadrants
            elif region.upper() == "NW" and lat >= 0 and lon < 0:
                filtered_points.add((lon, lat))
            elif region.upper() == "NE" and lat >= 0 and lon >= 0:
                filtered_points.add((lon, lat))
            elif region.upper() == "SW" and lat < 0 and lon < 0:
                filtered_points.add((lon, lat))
            elif region.upper() == "SE" and lat < 0 and lon >= 0:
                filtered_points.add((lon, lat))

        if filtered_points:
            filtered_coverage[level] = filtered_points

    return filtered_coverage


def get_map_bounds(coverage, region=None):
    """Get appropriate map bounds based on coverage and region."""
    if not coverage:
        return (-180, 180, -90, 90)  # Default to world map

    # Set initial bounds based on region
    if region == "N":
        min_lat, max_lat = 0, 90
        min_lon, max_lon = -180, 180
    elif region == "S":
        min_lat, max_lat = -90, 0
        min_lon, max_lon = -180, 180
    elif region == "E":
        min_lat, max_lat = -90, 90
        min_lon, max_lon = 0, 180
    elif region == "W":
        min_lat, max_lat = -90, 90
        min_lon, max_lon = -180, 0
    elif region == "NW":
        min_lat, max_lat = 0, 90
        min_lon, max_lon = -180, 0
    elif region == "NE":
        min_lat, max_lat = 0, 90
        min_lon, max_lon = 0, 180
    elif region == "SW":
        min_lat, max_lat = -90, 0
        min_lon, max_lon = -180, 0
    elif region == "SE":
        min_lat, max_lat = -90, 0
        min_lon, max_lon = 0, 180
    else:
        # If no region specified, use data bounds with padding
        all_points = []
        for points in coverage.values():
            all_points.extend(points)

        if not all_points:
            return (-180, 180, -90, 90)

        lons = [p[0] for p in all_points]
        lats = [p[1] for p in all_points]

        padding = 5  # degrees of padding
        min_lon = max(min(lons) - padding, -180)
        max_lon = min(max(lons) + padding, 180)
        min_lat = max(min(lats) - padding, -90)
        max_lat = min(max(lats) + padding, 90)

    return (min_lon, max_lon, min_lat, max_lat)


def plot_coverage(coverage, output_file=None, show_grid=True, region=None):
    """Plot the DTED coverage on a map."""
    fig, ax = plt.subplots(figsize=(12, 8))

    # Filter data by region if specified
    filtered_coverage = filter_by_region(coverage, region)

    # Get appropriate map bounds
    min_lon, max_lon, min_lat, max_lat = get_map_bounds(filtered_coverage, region)

    # Set up the map
    ax.set_xlim(min_lon, max_lon)
    ax.set_ylim(min_lat, max_lat)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    # Set title based on region
    title = "DTED Coverage Map"
    region_names = {
        "N": "Northern Hemisphere",
        "S": "Southern Hemisphere",
        "E": "Eastern Hemisphere",
        "W": "Western Hemisphere",
        "NW": "Northwest Quadrant",
        "NE": "Northeast Quadrant",
        "SW": "Southwest Quadrant",
        "SE": "Southeast Quadrant",
    }

    if region:
        title += f" - {region_names.get(region.upper(), region)}"
    ax.set_title(title)

    # Add grid lines
    if show_grid:
        # Determine appropriate grid spacing based on map extent
        lon_span = max_lon - min_lon
        lat_span = max_lat - min_lat

        if lon_span <= 10:
            lon_major, lon_minor = 1, 0.1
        elif lon_span <= 50:
            lon_major, lon_minor = 5, 1
        else:
            lon_major, lon_minor = 10, 1

        if lat_span <= 10:
            lat_major, lat_minor = 1, 0.1
        elif lat_span <= 50:
            lat_major, lat_minor = 5, 1
        else:
            lat_major, lat_minor = 10, 1

        ax.grid(True, linestyle="--", alpha=0.7)
        ax.set_xticks(
            np.arange(
                math.ceil(min_lon / lon_major) * lon_major,
                math.floor(max_lon / lon_major) * lon_major + lon_major,
                lon_major,
            )
        )
        ax.set_yticks(
            np.arange(
                math.ceil(min_lat / lat_major) * lat_major,
                math.floor(max_lat / lat_major) * lat_major + lat_major,
                lat_major,
            )
        )

        if lon_minor > 0:
            ax.xaxis.set_minor_locator(MultipleLocator(lon_minor))
        if lat_minor > 0:
            ax.yaxis.set_minor_locator(MultipleLocator(lat_minor))

        ax.grid(True, which="minor", linestyle=":", alpha=0.4)

    # Define colors for different DTED levels
    colors = {
        0: "yellow",
        1: "green",
        2: "blue",
    }

    # Create legend handles
    legend_handles = []

    # Plot each DTED level
    for level in sorted(filtered_coverage.keys()):
        points = filtered_coverage[level]
        color = colors.get(level, "gray")

        for lon, lat in points:
            # Plot 1x1 degree cell
            rect = mpatches.Rectangle(
                (lon, lat),
                1,
                1,
                alpha=0.7,
                facecolor=color,
                edgecolor="black",
                linewidth=0.5,
            )
            ax.add_patch(rect)

        # Add to legend
        legend_handles.append(mpatches.Patch(color=color, label=f"DTED Level {level}"))

    # Add the legend
    if legend_handles:
        ax.legend(handles=legend_handles, loc="lower right")

    # Save the figure if output file is specified
    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches="tight")
        print(f"Coverage map saved to {output_file}")

    # Show the figure
    plt.tight_layout()
    plt.show()


def print_region_summary(coverage, region=None):
    """Print summary of coverage, filtered by region if specified."""
    if region:
        filtered = filter_by_region(coverage, region)
        filtered_total = sum(len(cells) for cells in filtered.values())

        print(f"\nFiltered by {region} region:")
        for level, cells in filtered.items():
            count = len(cells)
            print(f"  Level {level}: {count} cells")
        print(f"  Total: {filtered_total} cells")

        if filtered_total == 0:
            print(f"No data found in the {region} region.")
            return False
        return True
    else:
        total_cells = sum(len(cells) for cells in coverage.values())
        return total_cells > 0


def main():
    parser = argparse.ArgumentParser(
        description="Visualize DTED data coverage from a directory structure."
    )
    parser.add_argument(
        "directory", help="Directory containing DTED data in format w115/n32.dt2"
    )
    parser.add_argument(
        "--output", "-o", help="Output file path (e.g., coverage_map.png)"
    )
    parser.add_argument("--no-grid", action="store_true", help="Disable grid lines")
    parser.add_argument(
        "--region",
        "-r",
        choices=["N", "S", "E", "W", "NW", "NE", "SW", "SE"],
        help="Filter by region (N=North, S=South, E=East, W=West, or combinations for quadrants)",
    )

    args = parser.parse_args()

    print(f"Scanning directory: {args.directory}")
    coverage = scan_directory(args.directory)

    # Print summary of all data
    print("\nDTED Coverage Summary:")
    total_cells = 0
    for level, cells in coverage.items():
        count = len(cells)
        total_cells += count
        print(f"  Level {level}: {count} cells")
    print(f"  Total: {total_cells} cells")

    if total_cells == 0:
        print("No DTED data found. Check your directory structure.")
        return

    # Print region-specific summary if requested
    has_data = print_region_summary(coverage, args.region)

    if not has_data:
        return

    # Plot the coverage
    plot_coverage(coverage, args.output, not args.no_grid, args.region)


if __name__ == "__main__":
    main()
