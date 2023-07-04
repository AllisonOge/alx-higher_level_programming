#!/usr/bin/python3
"""module for simple rectangular class"""


class Rectangle:
    """This class represent a rectangle."""
    number_of_instances = 0
    def __str__(self):
        """customize print for instance of class"""
        if self.width == 0 or self.height == 0:
            return ""
        return self.disp()

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle class

        Args:
            width (integer): value of the width
            height (integer): value of the height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def disp(self):
        """display the class object in style

        Returns: formatted string
        """
        s = ""
        for _ in range(self.height - 1):
            s += "{}\n".format("#" * self.width)
        s += "{}".format("#" * self.width)
        return s

    def __repr__(self):
        """clear string implementation of an rect object
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Delete an instance of the class
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
