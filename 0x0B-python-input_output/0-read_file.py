#!/usr/bin/python3
"""
module to read a utf-8 encoding text file
"""


def read_file(filename=""):
    """
    Reads a text file and prints to stdout

    Args:
        filename (string): absolute or relative path to file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
