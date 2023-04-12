#!/usr/bin/python3
""" function to print JSON representation of an object (string) """
import json

def to_json_string(my_obj):
    """ return JSON rep of an object (string)

    Args:
        my_obj (str): the string to serialize

    Returns:
        the JSON representation
    """

    return (json.dumps(my_obj))
