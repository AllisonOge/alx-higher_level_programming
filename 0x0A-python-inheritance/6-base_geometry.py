#!/usr/bin/python3
"""
module to create a base class
"""


class BaseGeometry:
    """This the class of base geometry"""
    def area(self):
        raise Exception("area() is not implemented")
