#!/usr/bin/python3
""" dictionary description for JSON serialization of an object """
import json


def class_to_json(obj):
    """ Function to generate dictionary desc of object in JSON format

    Args:
        obj: the object to describe

    Returns:
        the description
    """
    return (obj.__dict__)
