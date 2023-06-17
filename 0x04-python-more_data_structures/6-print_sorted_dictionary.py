#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    for k, v in dict(sorted(a_dictionary.items())).items():
        print("{}:".format(k), v)
