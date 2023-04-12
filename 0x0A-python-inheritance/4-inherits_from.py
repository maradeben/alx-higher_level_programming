#!/usr/bin/python3
""" check obj was inherited from superclass """


def inherits_from(obj, a_class):
    """ Checks that obj is instance of class
        inherited directly or indirectly from the specified class

    Args:
        obj: the class
        a_class: the parent

    Returns:
        True
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
