#!/usr/bin/python3
def process_tuple(tuple):
    if (len(tuple) == 0):
        return (0, 0)
    if (len(tuple) == 1):
        return (tuple[0], 0)
    return (tuple[0], tuple[1])


def add_tuple(tuple_a=(), tuple_b=()):
    a_0, a_1 = process_tuple(tuple_a)
    b_0, b_1 = process_tuple(tuple_b)

    return ((a_0 + b_0, a_1 + b_1))
