#!/usr/bin/python3
"""
module that compares an instance of a class
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class otherwise False

    Args:
        obj (object): object of a class
        a_class (class): class structure

    Returns:
        (boolean): True or False
    """
    return issubclass(type(obj), a_class) and not type(obj) == a_class
