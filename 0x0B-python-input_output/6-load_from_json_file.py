#!/usr/bin/python3
"""
module for reading JSON string from file
"""
import json


def load_from_json_file(filename):
    """
    Loads a python object from a JSON string

    Args:
        filename (string): filename or path to file (absolute or relative)
    """
    with open(filename, encoding="utf-8") as f:
        json.load(f)
