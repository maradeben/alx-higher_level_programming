#!/usr/bin/python3
""" Implementation of Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class inheriting from Rectangle """
    def __init__(self, size):
        """ initializing square class, overriding parent class' init"""

        super().__init__(size, size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)
