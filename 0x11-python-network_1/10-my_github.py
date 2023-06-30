#!/usr/bin/python3
""" take GitHub credentials, use GitHub API to display id """
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'

    r = requests.get(url, auth=(username, password))
    if r.status_code == 200:
        print(r.json().get('id'))
    else:
        print("None")
