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
    i = 0

    while True:
        try:
            if i < x:
                print(my_list[i], end='')
                i+=1
            else:
                print()
                return(i)
        except IndexError:
            print('')
            return (i)
    print('')
    return (i + 1)
