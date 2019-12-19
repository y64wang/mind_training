#!/bin/bash

#set -o verbose
#set -o xtrace
set -o errexit
set -o pipefail
set -o errtrace
set -o nounset

if [ "$#" -ne 1 ]; then
    echo "$0 on|off"
    exit 1
fi

if [ $1 == "on" ]; then
    sed -i '/arch=cevaxc4500/s/$/ -save-temps/g' C_Application/SC_UL_PHY_LF/Make/CevaCompilationFlags.mk
else
    sed -i '/arch=cevaxc4500/s/ -save-temps//g' C_Application/SC_UL_PHY_LF/Make/CevaCompilationFlags.mk
fi
