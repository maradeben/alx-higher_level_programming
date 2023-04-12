#!/usr/bin/python3
""" contains function to creates Object from JSON file """
import json


def load_from_json_file(filename):
    """ Crate Object from a "JSON file"

    Args:
        filename (str): the name of JSON file

    Returns:
        the created Object
    """

    with open(filename, 'r') as f:
        json_object = json.load(f)

    return (json_object)
