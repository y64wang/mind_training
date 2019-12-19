#!/bin/bash

#set -x

if [ "$#" -lt 1 ]; then
    echo "$0 userid ..."
    exit 1
fi

for var in "$@"
do
    echo -n "$var: "
    ldapsearch -H ldaps://ed-p-gl.emea.nsn-net.net -x -b ou=People,o=NSN "uid=$var" |grep "cn"
    if [ "$?" -eq 1 ]; then echo; fi
done
