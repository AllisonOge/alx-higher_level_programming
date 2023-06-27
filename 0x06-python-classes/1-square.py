#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module for Square class with attribute size"""


class Square:
    """This calss represents a square."""
    def __init__(self, size):
        """
        Initialize a Square object.

        Args:
            size (any): the length of the square's sides
        """
        self.__size = size
