#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
from requests import get

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    re = get(url)
    print('Body response:')
    print(f'\t- type: {type(re.text)}')
    print(f'\t- content: {re.text}')
