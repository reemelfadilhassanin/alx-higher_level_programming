#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the value 
    """
from sys import argv
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = argv[1]

    re = Request(url)
    with urlopen(re) as response:
        print(dict(response.headers).get("X-Request-Id"))
