#!/bin/bash

#set -o verbose
#set -o xtrace
set -o errexit
set -o pipefail
set -o errtrace
set -o nounset

if [ "$#" -ne 2 ]; then
    echo "$0 filetype pattern"
    exit 1
fi

sed -e 's/ /\n/g' lteDo/libDspCommon/dsplf_abic/release/Algorithms/BlockDecoder/.MaxSearch.cpp.o.cmd > dir.list
sed -i '/^-I/!d' dir.list
sed -i 's/^-I//g' dir.list
sort -u dir.list | xargs -I{} find {} -name "$1" -type f -print0 | xargs -0 grep -in "$2" --color=auto

