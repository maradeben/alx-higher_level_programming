#!/usr/bin/python3
""" contains function to read a text file """


def read_file(filename=""):
    """ program to read and print UTF8 text file

    Args:
        filename (str): name of file

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        contents = f.read()

    print(contents, end="")
