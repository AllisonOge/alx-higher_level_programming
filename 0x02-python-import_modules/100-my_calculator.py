#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


if __name__ == "__main__":
    n_args = len(sys.argv) - 1

    if n_args != 3:
        sys.stdout.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if op not in ["+", "-", "*", "/"]:
        sys.stdout.write("Unknown operator. Available operators: +, -, * and /\n")
        exit(1)

    result = 0
    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)

    print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))
