#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """
    @fct: a pointer to a function
    @args: arguments
    Description: safely execute a function
    Return: the result of the function if successful
    Otherwise, returns None if some error occurs, prints it in stderr
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
