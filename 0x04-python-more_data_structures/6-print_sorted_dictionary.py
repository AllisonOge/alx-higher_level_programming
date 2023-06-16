#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for k, v in dict(sorted(a_dictionary.items(), key=lambda i: i[0])).items():
        print("{}: ".format(k), v)
