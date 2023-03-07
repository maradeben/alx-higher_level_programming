#!/usr/bin/python3
"""
Returns the last digit of a number
"""


def print_last_digit(number):
    if number < 0:
        last = (-1 * number) % 10
    else:
        last = number % 10
    print(last, end='')

    return last
