#!/usr/bin/python3
"""Python script that takes your GitHub credentials 
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    re = requests.get(url, auth=(username, password))

    if re.status_code == 200:
        user_info = re.json()
        print(user_info['id'])
    else:
        print(None)
