#!/usr/bin/python3
"""
module to add a new attribute to an object if possible
"""


def add_attribute(obj, name, value):
    """
    Add a new attribute if possible

    Args:
        obj (object): instance of a class
        name (string): name of attribute
        value (any): value of attribute

    Raises:
        TypeError: if object can't have anew attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
