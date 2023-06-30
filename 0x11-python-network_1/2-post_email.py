#!/usr/bin/python3
""" take a URL and email, send POST request to URL
    with email as parameter, display body of response
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    params = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(params).encode('ascii')
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen((req)) as response:
        resp = response.read()
    print(resp.decode('utf-8'))
