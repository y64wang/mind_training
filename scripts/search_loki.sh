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


grep "INCLUDES" out/build-clang64/build.ninja | tail -1 | sed -e "s/ /\n/g" > dir.list
sed -i '/^.*\.\.\//!d' dir.list
sed -i 's/^-I//g' dir.list
sed -i 's/\.\.\/\.\.\///g' dir.list
awk  '{ if (! system("test -d " $0)) print $0}' dir.list | xargs -I{} find {} -name "$1" -type f -print0 | xargs -0 grep -in "$2" --color=auto

