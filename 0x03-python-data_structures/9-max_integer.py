#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    maxim = 100_000_000 * -1
    for element in my_list:
        if element > maxim:
            maxim = element
    return maxim
