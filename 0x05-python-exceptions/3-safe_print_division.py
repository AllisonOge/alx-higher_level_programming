#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
        print("Inside result:", end=" ")
    except ZeroDivisionError:
        print("Inside result:", end=" ")
    finally:
        print(result)
