#!/usr/bin/python3

def safe_print_integer(value):
    """
    print an integer with "{:d}".format() followed by a new line
    Return True is value has been printed (i.e, it's an integer
    Return False otherwise
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
