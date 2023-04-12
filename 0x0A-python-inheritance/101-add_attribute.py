#!/usr/bin/python3
""" add attribute """


def add_attribute(a_class, name, value):
    """ Add attribute to a class if possible.
        Raise exception otherwise

    Args:
        a_class: the class to add attribute to
        name (str): name of attribute
        value

    Raises:
        TypeError: if a_class can't have new attribute

    Returns:
        None
    """

    if not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(a_class, name, value)
