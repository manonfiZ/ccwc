#!/bin/bash

read data

exit_code=$?

if [ $exit_code -ne 0 ]; then
    exit $exit_code
fi

if [ -n "$data" ] ;
then
    tempFile=$(mktemp)
    cat > $tempFile
    python3 ./main.py  $tempFile $1
else
    python3 ./main.py  $1 $2
fi
