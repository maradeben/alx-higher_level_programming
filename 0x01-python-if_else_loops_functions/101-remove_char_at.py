#!/usr/bin/python3
def remove_char_at(str, n):
    str = [c for c in str if str.index(c) != n]
    return (''.join(str))
