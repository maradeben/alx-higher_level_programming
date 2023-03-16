#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    new_dict = {key: value for key, value in a_dictionary.items()}
    new_dict = {key: value * 2 for key, value in new_dict.items()}
    return (new_dict)
