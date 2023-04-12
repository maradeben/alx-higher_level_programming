#!/usr/bin/python3
""" save JSON to a text file """
import json


def save_to_json_file(my_obj, filename):
    """ Save JSON to a file

    Args:
        my_obj (str): the JSON object
        filename (str): name of file to save to

    Returns:
        None
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
