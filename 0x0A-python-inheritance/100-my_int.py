#!/usr/bin/python3
"""
module for my int class
"""


class MyInt(int):
    """This is the class for myint"""
    def __eq__(self, other):
        """Returns True if not equal otherwise False"""
        return self.real != other.real

    def __ne__(self, other):
        """Returns True if equal and False otherwise"""
        return self.real == other.real
