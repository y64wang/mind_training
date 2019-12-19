#!/bin/bash
rm -rf lteDo/HwPackage/

make prepall

make build_hw_abic ENABLE_PROFILING=2 NUMBER_OF_CEVA_CORES=1

make build_tenv

