#!/usr/bin/python3
def remove_char_at(s, n):
    s_new = ""
    for i, c in enumerate(s):
        if i != n:
            s_new += c
    return s_new
