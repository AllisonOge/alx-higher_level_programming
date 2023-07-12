#!/usr/bin/python3
"""
module to serialize python class to JSON
"""


def class_to_json(obj):
    """
    Returns the dictionary representation of a simple data structure

    Args:
        obj (object): python object

    Returns:
        (dictionary)
    """
    return obj.__dict__
