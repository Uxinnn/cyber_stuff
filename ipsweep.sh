#!/bin/bash

# Syntax: ./ipsweep.sh <network ip>

if [ "$1" == "" ]; then
    echo "Empty IP Address"
else
    for ip in `seq q 254`; do
        ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
    done
fi