#!/usr/bin/python3
""" Fetch https://alx-intranet.hbtn.io/status """
import urllib.request


url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    resp = response.read()

print("""Body response:
    - type: {}
    - content: {}
    - utf8 content: {}""".
      format(type(resp), resp, resp.decode('utf-8')))
