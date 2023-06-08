#!/usr/bin/python3
from add_0 import add
if __name__ == "__main__":
    # encapsulate code as main script
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
