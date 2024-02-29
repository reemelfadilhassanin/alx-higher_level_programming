#!/bin/bash
#  Bash script that sends a JSON POST request to a URL passed 
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
