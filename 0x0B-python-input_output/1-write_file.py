#!/usr/bin/python3
""" function to write text to a file """


def write_file(filename="", text=""):
    """ Write text to a file, with UTF-8 encoding
        Create if file doesn't exist, overwrite if it does

    Args:
        filename (str): name of file
        text (str): content to write

    Returns:
        (int): the number of characters written
    """

    with open(filename, 'w', encoding='utf-8') as f:
        count = f.write(text)

    return (count)
