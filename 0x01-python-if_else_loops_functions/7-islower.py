#!/usr/bin/python3
"""
Check if a character is lowercase. Return True if so, False otherwise
"""


def islower(c):
    if ord(c) >= 97 and ord(c) <= (122):
        return True
    else:
        return False
