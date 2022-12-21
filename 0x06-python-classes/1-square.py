#!/usr/bin/python3

""" Square class
Module for representing a Square object
"""


class Square:
    """This is a class to represent a Square object.

    It has no public attributes

    Attributes:
        size (int): Size of square

    """

    def __init__(self, size):
        """The initialization function simply sets the size

        __init__ is implicitly called on instantiating a Square object

        Args:
            size (int): Size of square
        """
        self.__size = size
