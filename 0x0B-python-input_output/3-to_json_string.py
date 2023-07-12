#!/usr/bin/python3
"""
module for serializing python objects to JSON
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object

    Args:
        my_obj (object): python object

    Returns:
        (string): JSON representation
    """
    return json.dumps(my_obj)
