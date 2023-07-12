#!/usr/bin/python3
"""
module that defines student class
"""


class Student:
    """This is the student class"""
    def __init__(self, first_name, last_name, age):
        """Constructor function for new instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the student instance
        """
        return self.__dict__
