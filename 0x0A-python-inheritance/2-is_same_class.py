#!/usr/bin/python3
"""
module to compare instance of a class
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified
    class otherwise False

    Args:
        obj (object): object of a class
        a_class (class): class structure

    Returns:
        (boolean): True or False
    """
    return type(obj) == a_class
