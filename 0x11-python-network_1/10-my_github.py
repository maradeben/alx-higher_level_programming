#!/usr/bin/python3
""" take GitHub credentials, use GitHub API to display id """
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(r.json()['id'])
