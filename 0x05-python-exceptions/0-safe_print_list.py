#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    for i, val in enumerate(my_list):
        if i >= x:
            break
        try:
            num += 1
            print(val, end="")
        except IndexError:
            break
    print()
    return num
