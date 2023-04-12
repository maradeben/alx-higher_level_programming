#!/usr/bin/python3
""" search and insert """


def append_after(filename="", search_string="", new_string=""):
    """ function to insert a line of text to a file,
            after each line containing a specific string

    Args:
        filename (str): name of file = ""
        search_string (str): string to search = ""
        new_string (str): string to insert = ""

    Returns:
        None
    """
    with open(filename, 'r') as file:
        contents = file.readlines()

    with open(filename, 'w') as file:
        for index, text in enumerate(contents):
            file.write(text)
            if text.__contains__(search_string):
                file.write(new_string)
