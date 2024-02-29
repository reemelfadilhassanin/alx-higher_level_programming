#!/bin/bash
# Send a POST request to 0.0.0.0:5000/catch_me
curl -sX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
