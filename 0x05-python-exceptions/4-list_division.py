#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    divide elements of my_list_1 by those of my_list_2
    number of elements to divide is list_length
    if division can't be done, set result to zero
    if element is not integer or float, print 'wrong type'
    on division by zero, print 'division by zero'
    if my_list_1 or _2 is too short, print 'out of range'
    return new list of results
    """

    result_list = []
    result = 0
    n = 0

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            result_list.append(result)
            n += 1
    return (result_list)
