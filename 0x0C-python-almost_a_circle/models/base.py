#!/usr/bin/python3
"""
module for the base class
"""


class Base:
    """The is the base class. It manages the id attribute for all classes"""
    __nb_objects = 0  # private static variable to track number of instances

    def __init__(self, id=None):
        """
        Initialize the class instance

        Args:
            id (int): identifier of the class instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
