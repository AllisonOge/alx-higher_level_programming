#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            _ = iter(my_list[i])
            continue
        except TypeError:
            try:
                print("{:d}".format(int(my_list[i])), end="")
                num += 1
            except ValueError:
                continue
    print()
    return num
