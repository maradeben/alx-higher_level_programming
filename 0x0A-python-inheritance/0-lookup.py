#!/usr/bin/python3
""" Module contains function to print attr and methods of object """


def lookup(obj):
    """ Function to list all avaiable attributes and methods of an object

    Args:
        obj: attribute/method to lookup

    Return:
        list of available methods and attributes
    """
    return (dir(obj))
