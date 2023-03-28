#!/usr/bin/python3

""" Square class
Module for representing a Square object
"""


class Square:
    """This is a class to represent a Square object.

    It has no public attributes

    """

    def __init__(self, size=0):
        """The initialization function simply sets the size

        __init__ is implicitly called on instantiating a Square object.

        Args:
            size (int): Size of square, defaults to 0

        Raises:
            TypeError: if size is not of type int
            ValueError: if size less than 0
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
