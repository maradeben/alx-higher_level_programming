#!/usr/bin/python3
""" contains function to check isinstance """


def is_same_class(obj, a_class):
    """ Checks if object is instance of a class

    Args:
        obj: the object to check
        a_class: class to check against

    Returns:
        True if isinstance, False otherwise
    """
    return (isinstance(obj, a_class))
