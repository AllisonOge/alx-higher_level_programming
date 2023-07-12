#!/usr/bin/python3
"""
module to inserts a new string after a certian substring in text file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific
    string

    Args:
        filename (string): filename or path to file
        search_string (string): search substring
        new_string (string): text to insert
    """
    with open(filename, mode="r+", encoding="utf-8") as f:
        lines  = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()

