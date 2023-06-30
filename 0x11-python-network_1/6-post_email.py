#!/usr/bin/python3
""" take email and url from command line
    send POST request to url with email as parameter
    display body of response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    params = {'email': sys.argv[2]}
    r = requests.post(url, data=params)
    print(r.text)
