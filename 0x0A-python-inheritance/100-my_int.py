#!/usr/bin/python3
""" MyInt class """


class MyInt(int):
    """ MyInt is a rebel class that has the == and != inverted """

    def __eq__(self, other):
        """ Equal to: inverted """
        return self.real != other

    def __ne__(self, other):
        """ Not equal: inverted """
        return self.real == other
