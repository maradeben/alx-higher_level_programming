#!/usr/bin/python3


def read_file(filename=""):
    """ program to read and print UTF8 text file

    Args:
        filename (str): name of file

    Returns:
        None
    """
    with open(filename) as f:
        contents = f.read()

    print(contents)
