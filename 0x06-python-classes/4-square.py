#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module that defines a class
with private attribute size and public function area"""


class Square:
    """This class is a square."""
    def __init__(self, size=0):
        """Initialize a Square object.

        Args:
            size (integer): the length of the square's sides

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """accessor for attrubute size

        Returns: value of size of object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """accessor for attribute size

        Args:
            value (integer): new value for size

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square object

        Returns: area of square object
        """
        return (self.__size ** 2)
