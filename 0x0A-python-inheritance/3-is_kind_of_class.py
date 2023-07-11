#!/usr/bin/python3
"""
module to compare instance of a class
"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from the specified
    class otherwise False

    Args:
        obj (object): object of a class
        a_class (class): class structure

    Returns:
        (boolean): True or False
    """
    return isinstance(obj, a_class)
