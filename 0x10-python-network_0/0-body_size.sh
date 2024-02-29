#!/bin/bash
#  Bash script that takes in a URL, sends a request to that URL

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
printf "%s" "$(curl -s "$1")" | printf "%s" "$(wc -c)"
