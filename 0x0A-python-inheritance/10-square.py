#!/usr/bin/python3
"""
module to create a subclass of the rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a subclass of the rectangle class"""
    def __init__(self, size):
        """Constructor function"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
