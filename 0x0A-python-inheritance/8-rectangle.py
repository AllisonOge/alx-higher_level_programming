#!/usr/bin/python3
"""
module to create a base class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """This is a subclass fo the base geometry"""
    def __init__(self, width, height):
        """Constructor function"""
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
