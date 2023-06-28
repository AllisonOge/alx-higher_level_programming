#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module that defines a class
with private attribute size and position,
public function area and accessors"""


class Square:
    """This class is a square."""
    def __init__(self, size=0, position=(0,0)):
        """Initialize a Square object.

        Args:
            size (integer): the length of the square's sides
            position (tuple): coordinates of the square object

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """accessor for attribute position

        Returns: value of position attruibute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """accessor for attribute position

        Args:
            value (tuple): coordinate of the square object

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Computes the area of the square object

        Returns: area of square object
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square
        object with the character # if
        size is not zero otherwize an
        empty line
        """
        for _ in range(self.position[1]):
            print()
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("{}{}".format(' '*self.position[0], '#'*self.size))
