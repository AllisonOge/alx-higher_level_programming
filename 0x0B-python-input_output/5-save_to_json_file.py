#!/usr/bin/python3
"""
module for saving JSON serialized python object
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes JSON serialized python object to file

    Args:
        my_obj (object): python object
        filename (string): filename or path to file (relative or absolute)
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
