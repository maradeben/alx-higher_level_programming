#!/usr/bin/python3
""" Class inheriting from list """


class MyList(list):
    """ class my list that inherits from a list """
    def print_sorted(self):
        """ prints the list sorted """
        print(sorted(self))
