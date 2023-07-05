#!/usr/bin/python3
"""
module for text indentation code
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each `.`, `?`, or `:`

    Args:
        text (string): a corpius of text

    Raises:
        TypeError: if test is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    c = 0
    # Skip leading whitespaces
    while c < len(text) and text[c] == " ":
        c += 1
    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            # Skip trailing whitespaces and delimiters
            while c < len(text) and text[c] in " ?.:":
                c += 1
            print("\n")
        else:
            c += 1
