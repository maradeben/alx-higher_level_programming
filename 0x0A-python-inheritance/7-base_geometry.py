#!/usr/bin/python3
""" BaseGeometry Class """


class BaseGeometry:
    """ a class BaseGeometry """

    def __init__(self):
        pass

    def area(self):
        """" a complaining unimplemented method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates values

        Args:
            self(BaseGeometry): instance of class
            name(string)
            value(int): expected to be int

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
