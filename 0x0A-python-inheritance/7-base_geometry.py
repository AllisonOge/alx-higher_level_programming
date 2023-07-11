#!/usr/bin/python3
"""
module to create a base class
"""


class BaseGeometry:
    """This the class of base geometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not (type(value) == int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
