#!/usr/bin/python3
def no_c(my_string):
    parsed = ''
    for c in my_string:
        if ((c != 'c') and (c != 'C')):
            parsed += c
    return parsed
