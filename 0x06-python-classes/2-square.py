#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module that defines a class with private attribute size"""


class Square:
    """This class is a square."""
    def __init__(self, size=0):
        """Initialize a Square object.

        Args:
            size (integer): the length of the square's sides
        """
        try:
            self.__size = int(size)
        except (ValueError, TypeError):
            raise TypeError("size must be an integer")
        
        if self.__size < 0:
            raise ValueError("size must be >= 0")
