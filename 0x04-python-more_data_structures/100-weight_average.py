#!/usr/bin/python3

def weight_average(my_list=[]):
    total_weights = sum([w for _, w in my_list])
    return sum([v * w for v, w in my_list]
               )/total_weights if len(my_list) > 0 else 0
