#!/usr/bin/python3
""" send request to URL, display response body
    if status code is greater than or equal 400, print it
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
