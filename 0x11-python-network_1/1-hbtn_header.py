#!/usr/bin/python3
""" take url from command line, display X-Request-Id in header """
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_id = response.info().get('X-Request-Id')
print(x_id)
