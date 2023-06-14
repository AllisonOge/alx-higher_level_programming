#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    return set([elm for elm in set_1 | set_2
               if elm not in set_1.intersection(set_2)])
