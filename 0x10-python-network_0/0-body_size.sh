#!/bin/bash
#  Bash script that takes in a URL, sends a request to that URL

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi
curl -s "${1}" | wc -c
