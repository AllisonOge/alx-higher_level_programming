#!/usr/bin/python3
"""
module for print_square function
"""


def print_square(size):
    """Prints a square of a given size with the pound character #

    Args:
        size (integer): size of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("{}".format("#" * size))
