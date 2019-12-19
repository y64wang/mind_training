#!/bin/bash

echo "2MB-hugepage usage:"
for pid in $(ps -ef | awk '{print $2}')
do
    if [[ -f /proc/$pid/smaps ]]
    then
        nr_hugepage=$(grep -B 16 'KernelPageSize:     2048 kB' /proc/$pid/smaps | grep -B 1 "^Size:"   | awk 'BEGIN{sum=0}{sum+=$2}END{print sum/2048}')
        if [[ $nr_hugepage -gt 0 ]]
        then
            cat /proc/$pid/cmdline
            echo " $pid: $nr_hugepage"
        fi
    fi
done

