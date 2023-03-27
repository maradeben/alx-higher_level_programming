#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    prints x items of a list

    Args:
        my_list (list): [],
        x (int): 0

    Returns:
        the number of arguments printed
    """

    if x == 0:
        print()
        return (0)

    for i in range(x):
        try:
            print(my_list[i], end='')
        except IndexError:
            print('')
            return (i)
    print('')
    return (i + 1)
