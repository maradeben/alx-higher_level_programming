#!/usr/bin/python3
"""Indent string"""


def text_indentation(text):
    """Prints text with 2 new lines after each of these characters
        '.', '?', ':'

    Arguments:
        text (str): the string to print

    Raises:
        TypeError: if text is not a string

    Returns:
        no return, only prints
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']

    for i in range(len(text)):
        if text[i] in chars:
            print(text[i], end="\n\n")
        elif text[i] == ' ' and text[i-1] in chars:
            while (text[i] == ' '):
                i += 1
        else:
            print(text[i], end='')
