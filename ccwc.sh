#!/bin/bash

read data

exit_code=$?

if [ $exit_code -ne 0 ]; then
    exit $exit_code
fi

if [ -n "$data" ] ;
then
    temp_file=$(mktemp)
    cat > $temp_file
    python3 ./main.py  $temp_file $1
else
    python3 ./main.py  $1 $2
fi
