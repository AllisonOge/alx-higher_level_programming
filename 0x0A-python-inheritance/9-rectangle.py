#!/usr/bin/python3
"""
module to create a subclass of base class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a subclass of the base geometry"""
    def __init__(self, width, height):
        """Constructor function"""
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns the custom formatted string for class instance"""
        return "[{}] {:d}/{:d}".format(type(self).__name__, self.__width,
                                       self.__height)
