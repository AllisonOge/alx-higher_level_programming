#!/usr/bin/python3
"""
module for say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """Prints the fullname in the format <first name> <last name>

    Args:
        first_name (string): the first name
        last_name (string): the last name

    Raises:
        TypeError: if either the first_name and last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
