#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    access x elements of my_list
    print only the integers, skip others in silence
    exception occurs if x is greater than len(my_list)
    return number of integers printed"""

    no_ints = 0  # number of integers printed
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            no_ints += 1
        except (ValueError, TypeError):
            pass

    print('')

    return (no_ints)
