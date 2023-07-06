#!/usr/bin/python3
"""locked class module"""


class LockedClass:
    """The is the class that only allows the instantiation
    of objects with attribute first_name
    """

    __slots__ = ["first_name"]
