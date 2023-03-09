#!/usr/bin/python3
import sys


args = sys.argv[1:]  # get arguments without filename
num_args = len(args)
if (num_args == 0):
    print("{:d} arguments.".format(num_args))
else:
    if (num_args == 1):
        title = "argument"
    else:
        title = "arguments"
    print("{:d} {:s}:".format(num_args, title))
    for idx, arg in enumerate(args):
        print("{:d}: {:s}".format(idx + 1, arg))
