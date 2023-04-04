#!/usr/bin/python3

"""Rectangle Module
Represents a rectangle object
"""


class Rectangle:
    """ Rectangle class representing a rectangle object"""

    def __init__(self, width=0, height=0):
        """Initializing function

        Args:
            width (int): Width of the rectangle. optional, defaults to 0
            height (int): Height of rectangle. Optional, defaults to 0
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """getter method for __width

        Returns:
            width of rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter method for the __width

        Args:
            value (int): value of width to set
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for __height

        Returns:
            height of rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """setter method for the __height

        Args:
            value (int): value of width to set
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Instance method to calculate the area of the Rectangle

        Returns:
            the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Instance method to calculate the perimeter of the Rectangle

        Returns:
            the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))
