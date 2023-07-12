#!/usr/bin/python3
"""
module to deseralize JSON string to python object
"""
import json


def from_json_string(s_my_list):
    """
    Returns an object (Python data structure) given a JSON string

    Args:
        s_my_list (string): JSON string representation

    Returns:
        (object): python object
    """
    return json.loads(s_my_list)
