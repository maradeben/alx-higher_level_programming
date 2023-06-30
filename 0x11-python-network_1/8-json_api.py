#!/usr/bin/python3
""" takes in a letter and sends post request to URL
    if no arg, set q to empty
    if response is proper JSON, display
    could be invalid or empty too
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': sys.argv[1] if len(sys.argv) > 1 else ""}
    r = requests.post(url, data=params)
    try:
        r_dict = r.json()
        if not r_dict:
            print("No result")
        else:
            print("[{}] {}".format(r_dict['id'], r_dict['name']))
    except ValueError:
        print("Not a valid JSON")
