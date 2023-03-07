#!/usr/bin/python3
"""
Print a string in uppercase
"""


def uppercase(str):
    for char in str:
        asc = ord(char)  # char's ascii value
        if asc >= 97 and asc <= 122:
            char = chr(asc - 32)  # convert to upper
        print("{:s}".format(char), end='')
    print('')
