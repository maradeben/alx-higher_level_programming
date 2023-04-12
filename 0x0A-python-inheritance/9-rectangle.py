#!usr/bin/python3
""" Rectangle class inheriting from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class. Inherits from BaseGeometry """

    def __init__(self, width, height):
        """ initialize rectangle with width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """ returns area of rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ print info about rectangle """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
