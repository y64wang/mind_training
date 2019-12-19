#!/bin/bash

#set -x

if [ ! "$#" -eq 2 ]; then
    echo "$0 ecl_link rev"
    exit 1
fi

LASTREV=`svn info $1 | grep "Last Changed Rev" | cut -d ' ' -f 4`
echo "Last Rev: $LASTREV"

BASEREV=${2//[!0-9]/}
if [ $BASEREV == $LASTREV ]; then
    echo "No update"
    exit 0
fi

svn diff -r $2:$LASTREV $1 | awk '/+ECL_UP_COMMON/ || /+ECL_PS_REL/ || /+ECL_LFS_REL/ || /+ECL_TOOLSET/ || /+ECL_ISAR_XML/ || /+ECL_ENV/ || /+ECL_SACK_BASE/  || /+ECL_BM/ || /+ECL_GLOBAL_ENV/ || /+ECL_ISAR_GEN/ || /+ECL_MSGIDLTE/ || /+ECL_LTE_SCM/'
