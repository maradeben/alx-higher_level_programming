#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def print_usage():
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)


def get_func(op):
    if (op == '+'):
        return (add)
    elif (op == '-'):
        return (sub)
    elif (op == '*'):
        return (mul)
    elif (op == '/'):
        return (div)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if (__name__ == "__main__"):
    args = sys.argv[1:]

    if (len(args) != 3):
        print_usage()

    a = int(args[0])
    op = args[1]
    b = int(args[2])
    func = get_func(op)

    result = func(a, b)

    print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))
