#!/usr/bin/python3
def uppercase(s):
    upper = ""
    for c in s:
        if ord(c) in range(97, 123):
            upper += "{:c}".format(ord(c) - 32)
        else:
            upper += c
    print(upper)
