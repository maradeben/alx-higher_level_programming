#!/usr/bin/python3
""" Module implementing a Square object """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square, inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize a Square object """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[{}] ({}) {}/{} - {}".format
                (self.__class__.__name__, self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ getter method for size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter method for size """

        if (type(value) != int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("widht must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update with arbitrary number of args or kwargs """
        if args and len(args) != 0:
            for ind, arg in enumerate(args):
                if arg is None:
                    self.__init__(self.size, self.x, self.y)
                if ind == 0:
                    self.id = arg
                elif ind == 1:
                    self.size = arg
                elif ind == 2:
                    self.x = arg
                elif ind == 3:
                    self.y = arg

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ serialize Square info """
        return ({
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        })
