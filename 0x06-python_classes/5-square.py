#!/usr/bin/python3

""" Square class
Module for representing a Square object
"""


class Square:
    """This is a class to represent a Square object.

    It has no public attributes

    Attributes:
        area: Calculates and returns the area of the square
        my_print: Prints a square with '#' symbols

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

    def area(self):
        """Method to calculate area of self

        Returns:
            The area of the square
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """ getter method for private attribute __self

        Returns:
            the size of square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ setter method for private attribute __self
        Args:
            value (int): the value of size to set
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Print square with character '#'
        with size of the square. Print an empty line if size is 0
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print('')
