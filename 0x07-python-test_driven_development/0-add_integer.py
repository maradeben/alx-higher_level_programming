#!/usr/bin/python3
"""Module containing a simple addition function"""


def add_integer(a, b=98):
    """A simple function to add integers

    Arguments:
        a (int): number
        b (int): second number, defaults to 98

    Raises:
        TypeError: if a or b is neither int nor float

    Returns:
        the result of addition, as an int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # cast values to ints
    a = int(a)
    b = int(b)

    return (a + b)
