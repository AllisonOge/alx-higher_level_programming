#!/usr/bin/python3
"""
module to write append to a text file using utf-8 encoding
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file encoded with utf-8
    and returns the number of characters added

    Args:
        filename (string): filename or path to file (relative or absolute)
        text (string): string of text to write

    Returns:
        (integer): number of characters written
    """
    nchars = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        nchars = f.write(text)
    return nchars
