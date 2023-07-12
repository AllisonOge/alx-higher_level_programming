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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the student instance
        if attrs is a list of strings, only attribute names contained
        in this list must be retrieved otherwise, all attributes must
        be retrieved
        """
        if (type(attrs) == list and
                all(type(e) == str for e in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
