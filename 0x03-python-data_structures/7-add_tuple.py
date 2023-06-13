#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        s = [0, 0]
        for i in range(2):
            if len(tuple_a) == 0 and len(tuple_b) == 2:
                s[i] = tuple_b[i]
            elif len(tuple_a) == 2 and len(tuple_b) == 0:
                s[i] = tuple_a[i]
            elif len(tuple_a) == 1 and len(tuple_b) == 2:
                s[i] = tuple_a[0] + tuple_b[i]
            elif len(tuple_a) == 2 and len(tuple_b) == 1:
                s[i] = tuple_a[i] + tuple_b[0]
        return tuple(s)
    return tuple(sum(pair) for pair in zip(tuple_a[:2], tuple_b[:2]))
