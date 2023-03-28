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

    def __init__(self, size=0, position=(0, 0)):
        """The initialization function simply sets the size

        __init__ is implicitly called on instantiating a Square object.

        Args:
            size (int): Size of square, defaults to 0
            position (tuple of ints): cartesian position of square

        Raises:
            TypeError: if size is not of type int
            ValueError: if size less than 0
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter method for the position
        Returns:
            the position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """setter method for position
        Args:
            value (tuple): tuple of ints for position
        """
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) != int or type(value[1]) != int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Print square with character '#'
        with size of the square. Print an empty line if size is 0
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print('')
            for i in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size, end='')
                print('')

    def __str__(self):
        """Prints an instance of a square
        Has the same behaviour as my_print()

        Returns:
            a string literal of the square
        """

        literal = ''
        if self.__size == 0:
            return ('\n')
        else:
            literal += '\n'*self.__position[1]
            for i in range(self.__size):
                literal += ' ' * self.__position[0]
                literal += '#' * self.__size
                if i != self.__size - 1:
                    literal += '\n'

        return (literal)
