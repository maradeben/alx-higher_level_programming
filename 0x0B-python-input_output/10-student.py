#!/usr/bin/python3
""" Student module """


class Student:
    """ class representing a Student """

    def __init__(self, first_name, last_name, age):
        """ initialize a student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation """
        if attrs == None:
            return (self.__dict__)
        else:
            return ({k: self.__dict__[k] for k in self.__dict__ & attrs})
