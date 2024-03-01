#!/usr/bin/python3
"""
Python script that takes in a URL and an email address
"""


if __name__ == '__main__':
    from sys import argv
    from requests import post

    url = argv[1]
    email = argv[2]

    pay = {'email': email}
    respon = post(url, data=pay)
    print(respon.text)
