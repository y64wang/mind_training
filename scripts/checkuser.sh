#!/bin/bash

#set -x

KEYWORDS="/mail:/ || /cn:/"
KEYWORDS="/mail:/"

if [ "$#" -lt 1 ]; then
    echo "$0 userid ..."
    exit 1
fi

for var in "$@"
do
    #echo -n "$var: "
    ldapsearch -H ldaps://ed-p-gl.emea.nsn-net.net -x -b ou=People,o=NSN "uid=$var" | awk "$KEYWORDS" | cut -d " " -f 2
    if [ "$?" -eq 1 ]; then echo; fi
done
