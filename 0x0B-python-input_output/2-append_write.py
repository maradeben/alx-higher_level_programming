#!/usr/bin/python3
""" function to append to a file """


def append_write(filename="", text=""):
    """ Append text to a file
        Create if not exist, append text if exists

    Args:
        filename (str): name of file
        text (str): text to append

    Returns:
        Number of characters added
    """

    with open(filename, 'a', encoding='utf-8') as f:
        count = f.write(text)

    return (count)
