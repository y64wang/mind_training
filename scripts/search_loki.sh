#!/bin/bash

#set -o verbose
#set -o xtrace

if [ "$#" -ne 2 ]; then
    echo "$0 target pattern"
    exit 1
fi

if [ $1 == "cmake" ]; then
    find . \( -name CMakeLists.txt -o -name "*cmake" -o -name "*sh" -o -name "*py" \) -type f > file.list

elif [ -f out/build-$1/build.ninja ]; then
    grep "JdConfigurator.cpp.o" out/build-$1/build.ninja -A 6 |grep "INCLUDES" | sed -e "s/ /\n/g" > dir.list
    sed -i '/^.*\.\.\//!d' dir.list
    sed -i 's/^-I//g' dir.list
    sed -i 's/\.\.\/\.\.\///g' dir.list
    awk  '{ if (! system("test -d " $0)) print $0}' dir.list | xargs -I{} find {} \( -name '*.h' -o -name '*.hpp' \) -type f > file.list
else
    echo " out/build-$1/build.ninja doesn't exist!"
    exit 1
fi

sort -u file.list > file1.list
cat file1.list | xargs -I{} grep -Hin "$2" --color=auto {}

rm -f dir.list file.list file1.list

