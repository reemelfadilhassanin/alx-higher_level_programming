#!/usr/bin/python3
"""
 Python script that takes in a URL, sends a request to the URL 
"""

from sys import argv
from requests import get
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    re = requests.get(url)
    print(get(argv[1]).headers.get('X-Request-Id'))
