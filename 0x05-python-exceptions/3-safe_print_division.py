#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = int(a) / int(b)
        print("Inside result:", end=" ")
    except ZeroDivisionError:
        print("Inside result:", end=" ")
    finally:
        print("{}".format(result))
