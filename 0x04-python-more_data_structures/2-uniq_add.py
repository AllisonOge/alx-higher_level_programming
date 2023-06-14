#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = {}
    for elm in my_list:
        if elm not in uniq.keys():
            uniq[elm] = 1
    return sum(uniq.keys())
