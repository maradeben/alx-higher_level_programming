#!/usr/bin/python3

def roman_to_int(roman_string):

    mapper = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if not isinstance(roman_string, str):
        return (0)
    num = 0
    pc = 'I'    # set initial value of previous character at minimum

    for c in roman_string[::-1]:
        if mapper[c] >= mapper[pc]:
            num += mapper[c]
        else:
            num -= mapper[c]
        pc = c

    return (num)
