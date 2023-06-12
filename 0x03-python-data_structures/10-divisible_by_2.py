#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divisible = [False] * len(my_list)
    for i, elm in enumerate(my_list):
        if elm % 2 == 0:
            divisible[i] = True
    return divisible
