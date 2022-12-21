#!/usr/bin/python3

class Square:
    """This is a class to represent a Square object.

    It has no public attributes

    """

    def __init__(self, size):
        """The initialization function simply sets the size

        __init__ is implicitly called on instantiating a Square object

        Args:
            size: a private instance variable representing the length of side
        """
        self.__size = size
