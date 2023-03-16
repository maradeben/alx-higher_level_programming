#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    key_order = sorted(a_dictionary)

    for key in key_order:
        print("{:s}: {}".format(key, a_dictionary[key]))
