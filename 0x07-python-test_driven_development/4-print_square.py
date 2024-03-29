#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """Function to print a square of '#'s

    Arguments:
        size (int): size of square

    Raises:
        TypeError: if size is not an integer
            if size is a float and is less than 0
        ValueError: if size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
