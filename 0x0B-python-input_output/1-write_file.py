#!/usr/bin/python3
"""
module to write to a text file using utf-8 encoding
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file with utf-8 encoding
    and return the number of number of characters written

    Args:
        filename (string): filename or path to file (relative or absolute)

    Returns:
        (integer): number of characters written
    """
    nchars = 0
    with open(filename, mode="w", encoding="utf-8") as f:
        nchars = f.write(text)
    return nchars
