#!/usr/bin/python3
"""
module for the base class
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Serialize list of dictionaries to JSON
        """
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file

        Args:
            cls (class):
            list_objs (list): list of instances who inherits of Base
        """

        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            f.write(Base.to_json_string(list_objs))
