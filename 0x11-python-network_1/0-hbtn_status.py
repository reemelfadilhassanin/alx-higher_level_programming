#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    from urllib.request import urlopen, Request

    url = "https://alx-intranet.hbtn.io/status"
    re = Request(url)
    with urlopen(re) as res:
        content = res.read()

    print("Body response:")
    print(f"\t- type:", type(content))
    print(f"\t- content:", (content))
    print(f"\t- utf8 content:", content.decode('utf-8'))
