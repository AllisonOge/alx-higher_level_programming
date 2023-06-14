#!/usr/bin/python3

def search_replace(my_list, search, replace):
    return [replace if elm == search else elm for elm in my_list]
