#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
"""
from sys import argv
from requests import get

if __name__ == "__main__":
    data = get(argv[1])
    if data.status_code >= 400:
        print(f"Error code: {data.status_code}")
    else:
        print(data.text)
