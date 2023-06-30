#!/usr/bin/python3
""" use requests library to get X-Request-Id """
import requests
import sys

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io'
    r = requests.get(url)

    print(r.headers.get('X-Request-Id'))
