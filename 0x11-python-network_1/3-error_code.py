#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the body
"""
from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    try:
        with urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as err:
        print(f'Error code: {err.code}')
