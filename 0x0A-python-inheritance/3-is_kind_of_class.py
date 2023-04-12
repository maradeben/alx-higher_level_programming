#!/usr/bin/python3
""" to check if obj is isntance of,
    or instance of object inherited from a class
"""


def is_kind_of_class(obj, a_class):
    """ Check object or object of subclass of class

    Args:
        obj: the object to check
        a_class: the class to check against

    Returns:
        True or False
    """
    return (isinstance(obj, a_class))
