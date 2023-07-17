#!/usr/bin/python3
"""
module for the square class
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """This is the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a class instance

        Args:
            size (int): size
            x (int): x position
            y (int): y position
        """
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """Customize print for class instance

        Returns: formated string
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.width)
