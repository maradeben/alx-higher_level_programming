#!/usr/bin/python3
"""" track IP addresses stats """
import sys

i = 1
status_codes = {200: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
sum = 0

def printer():
    """ print stats """
    print("File size: {}".format(sum))
    for k in sorted(status_codes.keys()):
        if v == 0:
            continue
        print("{}: {}".format(k, status_codes[k]))

while True:    
    try:
        for line in sys.stdin:
            line = input()
            code = int(line.split()[-2])
            size = int(line.split()[-1])

            status_codes[code] += 1
            sum += size

            if i % 10 == 0:
                printer()
    except KeyboardInterrupt:
        printer()
        raise
    printer()
