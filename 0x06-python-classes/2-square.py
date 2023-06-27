#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module that defines a class with private attribute size"""


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
