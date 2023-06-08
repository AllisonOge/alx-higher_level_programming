#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n_args = len(sys.argv) - 1
    print("{} argument{}".format(n_args, '' if n_args == 1 else 's'), end="")
    print("{}".format('.' if  n_args == 0 else ':'))
    for i, arg in enumerate(sys.argv[1:]):
        print("{}: {}".format(i + 1, arg))
