#!/usr/bin/python3
""" function to return object represented by JSON string """
import json


def from_json_string(my_str):
    """ Returns object (Python data structure) represented by JSON string

    Args:
        my_str

    Returns:
        the object
    """

    return (json.loads(my_str))
