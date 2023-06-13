#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        return (0, 0)
    return tuple(tuple_a[i] + tuple_b[i] if i < len(tuple_a)
                 and i < len(tuple_b)
                 else (tuple_a[i] if i < len(tuple_a)
                 else (tuple_b[i] if i < len(tuple_b) else 0))
                 for i in range(2))
