#!/usr/bin/python3
"""module to add two integers"""


def add_integer(a, b=98):
    """returns the sum of two integers

    Args:
        a (integer): first integer
        b (integer): second integer

    Raises:
        TypeError: if a is not an integer or float
        TypeError: if b is not an integer or float

    Returns:
        (integer): sum of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int (b)
