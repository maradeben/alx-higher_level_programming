#!/usr/bin/python3
""" take GitHub credentials, use GitHub API to display id """
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/users/{}'.format(username)

    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    try:
        print(r.json()['id'])
    except ValueError:
        print("Not a valid JSON")
