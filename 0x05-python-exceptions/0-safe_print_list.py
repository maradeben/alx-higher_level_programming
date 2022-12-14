#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    prints x items of a list
    x may be higher than number of elements in list
    """
    for i in range(x):
        try:
            print(f"{my_list[i]}", end='')
        except IndexError:
            print('')
            return (i)
    print('')
    return (i + 1)
