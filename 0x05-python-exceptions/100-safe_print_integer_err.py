#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        _ = iter(value)
        raise ValueError
    except TypeError:
        try:
            print("{:d}".format(int(value)))
            return True
        except ValueError as err:
            print("Exception: {}".format(err), file=sys.stderr)
            return False
    except ValueError as err:
        print("Exception: {}".format(err), file=sys.stderr)
