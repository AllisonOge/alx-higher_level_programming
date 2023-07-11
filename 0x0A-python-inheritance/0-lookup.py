#!/usr/bin/python3
"""
module to lookup an object's attributes and methods
"""


def lookup(obj):
    """
    returns the list of available attributes and methods of an object

    Args:
        obj (object): object to be inspected

    Returns:
        (list): list of attributes and methods
    """
    return dir(obj)
