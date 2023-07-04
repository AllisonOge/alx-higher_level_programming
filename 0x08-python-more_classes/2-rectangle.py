#!/usr/bin/python3
"""module for simple rectangular class"""


class Rectangle:
    """This class represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle class

        Args:
            width (integer): value of the width
            height (integer): value of the height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """accessor for width property

        Returns: value of the width property
        """
        return self.__width

    @width.setter
    def width(self, value):
        """accessor for width property

        Args:
            value (integer): value of the width

        Raises:
            TypeError: if the value is not integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """accessor for height property

        Returns: value of height propery
        """
        return self.__height

    @height.setter
    def height(self, value):
        """accessor for height property

        Args:
            value (integer): value of the height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle

        Return: area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle

        Returns: perimeter of the rectangle
        """
        if self.width == 0 and self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)
