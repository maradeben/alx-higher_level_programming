#!/usr/bin/python3

import sys
import os


def safe_print_integer_err(value):
    """
    @value: the value passed in, can be any type
    print with safe printing for integers
    Return: True if value is printed (i.e, is an integer)
    Otherwise, return False and prints the error in stderr
    preceded by 'Exception:'
    """
    try:
        print(f"{value:d}")
        return True
    except ValueError as ve:
        # sys.stderr.write(f"Exception: {ve}")
        # os.write(2, f"Exception: {ve}")
        print(f"Exception: {ve}", file=sys.stderr)
        return False
