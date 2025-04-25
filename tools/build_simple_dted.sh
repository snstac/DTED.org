#!/bin/bash

echo "Building DTED index files..."

SRC_DTED="data/stream/elevation/DTED/dted_nw_hemi.zip"

for zipfile in data/src/*.zip; do
  dirname=$(basename "${zipfile}" .zip | cut -d'-' -f1)
  tmpdir=$(mktemp -d)

  echo "Processing ${zipfile} for ${dirname} under ${tmpdir}"

  echo "Unzipping ${zipfile} to ${tmpdir}"
  unzip -q "${zipfile}" -d "${tmpdir}"

  echo "Moving files to data/build/in/${dirname}"
  rm -rf data/build/in/"${dirname}"
  mkdir -p data/build/in/"${dirname}"
  mv "${tmpdir}"/*/* data/build/in/"${dirname}"

  echo "Overlaying ${SRC_DTED} files..."
  unzip -q "${SRC_DTED}" -d data/build/in/"${dirname}" || exit 1

  echo "Creating index for ${dirname}"
  rm -rf data/build/out/"${dirname}"
  python3 tools/create_index.py data/build/in/"${dirname}" data/build/out/"${dirname}"

  rm -rf "${tmpdir}"
done
