#!/usr/bin/python3
"""
module to print the content of a list object in ascending order
"""


class MyList(list):
    """This is a child class of the list object"""
    def print_sorted(self):
        """prints the list in ascending order"""
        list_cpy = self.copy()
        print(sorted(list_cpy))
