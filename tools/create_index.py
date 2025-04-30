#!/usr/bin/env python3

import os
import zipfile
import time


def zip_file(input_file, output_file):
    try:
        with zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.write(input_file, os.path.basename(input_file))
        return output_file
    except Exception as e:
        print(f"Error zipping the file: {input_file} - {e}")
        if os.path.exists(output_file):
            try:
                os.remove(output_file)
            except Exception as delete_error:
                print(
                    f"Failed to delete the output file {output_file} - {delete_error}"
                )
        return None


def write(filename, version, data):
    try:
        with open(filename, "w") as output_writer:
            output_writer.write(f"{version}\n")
            output_writer.write(f"{int(time.time() * 1000)}\n")
            for row in data:
                output_writer.write("".join(map(str, row)) + "\n")
    except Exception as e:
        print(f"Error writing to file {filename} - {e}")


def visualize_index(index_file):
    try:
        with open(index_file, "r") as f:
            lines = f.readlines()

        version = lines[0].strip()
        timestamp = lines[1].strip()
        data = lines[2:]

        print(f"Index File Version: {version}")
        print(f"Timestamp: {timestamp}")
        print("World Data Visualization:")

        for row in data:
            print("".join(row.strip()))
    except Exception as e:
        print(f"Error visualizing index file {index_file} - {e}")


def validate_index_file(index_file):
    try:
        with open(index_file, "r") as f:
            lines = f.readlines()

        version = lines[0].strip()
        timestamp = lines[1].strip()
        data = lines[2:]

        if not version.isdigit():
            print(f"Invalid version number: {version}")
            return False

        if not timestamp.isdigit():
            print(f"Invalid timestamp: {timestamp}")
            return False

        for row in data:
            if len(row.strip()) != 360:
                print(f"Invalid row length: {len(row.strip())}")
                return False

        print("Index file is valid.")
        return True
    except Exception as e:
        print(f"Error validating index file {index_file} - {e}")
        return False


def read_index_file(index_file):
    try:
        with open(index_file, "r") as f:
            lines = f.readlines()

        version = lines[0].strip()
        timestamp = lines[1].strip()
        data = lines[2:]

        world_data = []
        for row in data:
            world_data.append(list(map(int, row.strip())))

        return version, timestamp, world_data
    except Exception as e:
        print(f"Error reading index file {index_file} - {e}")
        return None, None, None


def write_index_file(index_file, version, timestamp, world_data):
    try:
        with open(index_file, "w") as f:
            f.write(f"{version}\n")
            f.write(f"{timestamp}\n")
            for row in world_data:
                f.write("".join(map(str, row)) + "\n")
    except Exception as e:
        print(f"Error writing index file {index_file} - {e}")
        return False
    return True


def main(input_dir, output_dir):
    if not os.path.exists(input_dir):
        print(f"Input directory does not exist: {input_dir}")
        return

    if os.path.exists(output_dir):
        print(f"Output directory cannot exist, please remove: {output_dir}")
        return

    try:
        os.makedirs(output_dir)
    except Exception as e:
        print(f"Output directory cannot be created: {output_dir} - {e}")
        return

    world = [[0 for _ in range(180)] for _ in range(360)]

    for ew_name in os.listdir(input_dir):
        ew_path = os.path.join(input_dir, ew_name)
        if not os.path.isdir(ew_path):
            continue

        if ew_name.lower().startswith(("w", "e")):
            ew_out = os.path.join(output_dir, ew_name)
            try:
                os.makedirs(ew_out)
            except Exception as e:
                print(f"Output directory cannot be created: {ew_out} - {e}")
                return

            index_html = os.path.join(ew_out, "index.html")
            try:
                with open(index_html, "w") as f:
                    pass
            except Exception as e:
                print(
                    f"Output dir listing blocker cannot be created: {index_html} - {e}"
                )
                return

            try:
                ew = int("".join(filter(str.isdigit, ew_name)))
                if ew_name.lower().startswith("w"):
                    ew *= -1

                for ns_name in os.listdir(ew_path):
                    ns_path = os.path.join(ew_path, ns_name)
                    if not os.path.isfile(ns_path):
                        continue

                    ns_name = ns_name.lower()
                    if ns_name.endswith((".dt0", ".dt1", ".dt2", ".dt3")):
                        print(
                            f"Encountered uncompressed elevation file: {ns_name} compressing..."
                        )
                        ns_out = os.path.join(ew_out, f"{ns_name}.zip")
                        if not zip_file(ns_path, ns_out):
                            continue
                        ns_name = os.path.basename(ns_out)
                    elif ns_name.endswith(
                        (".dt0.zip", ".dt1.zip", ".dt2.zip", ".dt3.zip")
                    ):
                        ns_out = os.path.join(ew_out, ns_name)
                        try:
                            with open(ns_path, "rb") as src, open(ns_out, "wb") as dst:
                                dst.write(src.read())
                        except Exception as e:
                            print(f"Error copying file {ns_path} to {ns_out} - {e}")
                            continue
                    else:
                        print(
                            f"Encountered unrecognized elevation file {ns_name} skipping..."
                        )
                        continue

                    try:
                        ns = int("".join(filter(str.isdigit, ns_name.split(".")[0])))
                        print(f"Processing file: {ns_name}, parsed ns value: {ns}")
                        if ns_name.startswith("s"):
                            ns *= -1

                        mask = 0
                        if "dt3" in ns_name:
                            mask = 4
                        elif "dt2" in ns_name:
                            mask = 2
                        elif "dt1" in ns_name:
                            mask = 1

                        # Debugging logs
                        print(f"ew: {ew}, ns: {ns}, mask: {mask}")
                        print(
                            f"Index in world array: ew + 180 = {ew + 180}, ns + 90 = {ns + 90}"
                        )

                        # Validate indices
                        if not (0 <= ew + 180 < 360) or not (0 <= ns + 90 < 180):
                            print(
                                f"Skipping out-of-bounds indices for ew: {ew}, ns: {ns}"
                            )
                            continue

                        world[ew + 180][ns + 90] |= mask
                    except Exception as e:
                        print(f"Error parsing file {ns_name} - {e}")
                        raise
            except Exception as e:
                print(f"Error processing directory {ew_name} - {e}")
                raise
    try:
        pre_index = os.path.join(output_dir, "index")
        zipped_index = os.path.join(output_dir, "index.zip")
        write(pre_index, 1, world)
        zip_file(pre_index, zipped_index)
        os.remove(pre_index)
    except Exception as e:
        print(f"Error occurred writing file: {e}")

    print(f"Constructed the layout for the server at: {output_dir}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print(
            "Usage:\n"
            "  python create_index.py [input directory] [output directory]\n\n"
            "The input directory must follow the required structure as described in the documentation."
        )
    else:
        main(sys.argv[1], sys.argv[2])
