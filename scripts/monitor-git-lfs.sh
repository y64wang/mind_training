#!/usr/bin/env bash

LFS="$(ps aux | grep git-lfs | grep -v grep | awk '{ print $2 }')";
SLEEP_INTERVAL="10";

while true; do
  PCPU="$(ps -p "$LFS" -o pcpu | tail -n 1 | awk '{ print $1 }')";
  PMEM="$(ps -p "$LFS" -o pmem | tail -n 1 | awk '{ print $1 }')";
  LSOF="$(lsof -p "$LFS" | wc -l | awk '{ print $1 }')";

  echo "$(date) - $PCPU\t$PMEM\t$LSOF";

  sleep "$SLEEP_INTERVAL";
done
