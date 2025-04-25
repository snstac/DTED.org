#!/bin/bash
# For ATAK DTED Stream Server, repack DTED to contain the state specific DTED2 data.

SRC_DTED="data/stream/elevation/DTED/dted_nw_hemi.zip"

for build_dir in data/build/out/*; do
  if [ -d "${build_dir}" ]; then 
      dirname=$(basename "${build_dir}") 
      tmpdir=$(mktemp -d)
      echo "Processing ${dirname} from ${build_dir} under ${tmpdir}"

      echo "Unzipping ${SRC_DTED} to ${tmpdir}"
      unzip -q "${SRC_DTED}" -d "${tmpdir}" || exit 1

      DST_ZIP="$(pwd)/data/stream/${dirname}/dted_nw_hemi.zip"
      mkdir -p data/stream/"${dirname}"
      rm -f "${DST_ZIP}"

      echo "Creating zip file ${DST_ZIP}"
      cd "${tmpdir}" || exit
      zip -qr "${DST_ZIP}" .
      rm -rf "${tmpdir}"
  fi
done