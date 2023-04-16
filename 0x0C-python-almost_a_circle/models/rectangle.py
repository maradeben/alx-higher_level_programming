#!/usr/bin/python3
""" Module implementing a Rectangle object """
from models.base import Base
import json


class Rectangle(Base):
    """ Rectangle class, inheriting from the Base Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize a Rectangle object """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for width """
        if self.validator("width", value, "dim"):
            self.__width = value

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height """
        if self.validator("height", value, "dim"):
            self.__height = value

    @property
    def x(self):
        """ getter method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method for x """
        if self.validator("x", value, "co-ord"):
            self.__x = value

    @property
    def y(self):
        """ getter method for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method for y """
        if self.validator("y", value, "co-ord"):
            self.__y = value

    def validator(self, name, value, par_type):
        """ validator method for values

        Args:
            self (Rectangle): rectangle object
            name (str): of attribute to validate
            value (int): to validate
            par_type (str): "dim"(dimension) or "co-ord"(co-ordinate)

        Raises:
            TypeError: if value is not of type int
            ValueError: if a dimension is 0 or less
                        or if a co-ordinate is less than 0

        Returns:
            True if all checks were passed
        """
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if par_type == "dim":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        elif par_type == "co-ord":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

        return True

    def area(self):
        """ returns the area of the rectangle """
        return (self.height * self.width)

    def display(self):
        """ displays the rectangle """
        display = ""
        display = '\n' * self.y

        for i in range(self.height):
            display += ' ' * self.x
            display += str('#') * self.width
            if i < self.height - 1:
                # only start newline if the last line has not been reached.
                # prevents extra line after the rectangle
                display += '\n'
        print(display)

    def __str__(self):
        """ overloading __str__ to print info about Rectangle """
        return ("[{}] ({}) {}/{} - {}/{}".format
                (self.__class__.__name__, self.id, self.x, self.y,
                 self.width, self.height))

    def update(self, *args, **kwargs):
        """ pass variable number of arguments """
        if args and len(args) != 0:
            for ind, arg in enumerate(args):
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                if ind == 0:
                    self.id = arg
                elif ind == 1:
                    self.width = arg
                elif ind == 2:
                    self.height = arg
                elif ind == 3:
                    self.x = arg
                elif ind == 4:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ convert to json dict """
        return ({
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.x,
            "y": self.y
        })
