#!/usr/bin/python3
"""
module for all test utility functions
"""
from io import StringIO
import sys


def getprintedoutput(obj, method=None):
    """Returns the captured output to stdout for a given object

    Args:
        obj (class) : instance of a class
        method (str): method to be called
    """
    # redirect the stdout to StringIO object
    captured_output = StringIO()
    sys.stdout = captured_output

    # dynamically call the method on the object if method is not None
    if method is None:
        print(obj)
    else:
        obj_method = getattr(obj, method)
        obj_method()

    # get the value printed to stdout
    actual_output = captured_output.getvalue()

    # reset stdout to its original value
    sys.stdout = sys.__stdout__
    return actual_output
