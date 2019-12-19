#!/bin/bash

#set -o verbose
#set -o xtrace
set -o errexit
set -o pipefail
set -o errtrace
set -o nounset

if [ "$#" -ne 2 ]; then
    echo "$0 rev1 rev2"
    exit 1
fi

svn diff https://svne1.access.nsn.com/isource/svnroot/BTS_SC_UP_COMMON/tags/FL00_UP_COMMON_0000_000000_000$1/C_Application/SC_UP_COMMON https://svne1.access.nsn.com/isource/svnroot/BTS_SC_UP_COMMON/tags/FL00_UP_COMMON_0000_000000_000$2/C_Application/SC_UP_COMMON
