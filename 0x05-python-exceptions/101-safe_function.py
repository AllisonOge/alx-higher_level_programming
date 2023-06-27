#!/usr/bin/python3
import sys

def safe_function(fct, *arg):
    try:
        ret_val = fct(*arg)
        return ret_val
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
