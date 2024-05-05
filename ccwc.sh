#!/bin/bash

if [ -f "$2" ] || [ -f "$1" ];
then
    python3 ./main.py  $1 $2
else
    temp_file=$(mktemp)
    file_content=$(cat)

    echo "$file_content" > $temp_file
    python3 ./main.py  $temp_file $1
fi
