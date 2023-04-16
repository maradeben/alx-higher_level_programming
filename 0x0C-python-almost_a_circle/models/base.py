#!/usr/bin/python3
""" Base Class """
import json
import os
import csv
import turtle


class Base:
    """ the base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize a Base class instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save documentation to file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write('[]')
            else:
                file.write(Base.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ load from json string """
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create class instance from dictionary """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            obj = Rectangle(3, 4)
        elif cls is Square:
            obj = Square(3)
        else:
            obj = None
        obj.update(dictionary)
        return obj
    
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r', encoding='utf-8') as f:
            return([cls.create(**kwargs)
                    for kwargs in cls.from_json_string(f.read())])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save object to csv file """
        from models.rectangle import Rectangle
        from models.square import Square

        filename = cls.__name__ + ".csv"
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[obj.id, obj.width, obj.height, obj.x, obj.y]\
                             for obj in list_objs]
            else:
                list_objs = [[obj.id, obj.size, obj.x, obj.y]\
                             for obj in list_objs]
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """ load object from csv file """
        from models.rectangle import Rectangle
        from models.square import Square

        filename = cls.__name__ + ".csv"
        objects = []
        with open(filename, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Square:
                    dic = {"id": row[0], "size": row[1], "x":row[2], "y": row[3]}
                else:
                    dic = {"id": row[0], "width": row[1], "height": row[2],\
                        "x": row[3], "y": row[4]}
                objects.append(cls.create(**dic))
        return objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw rectangle/square object with Python Turtle """
        t = turtle.Turtle()
        t.screen.bgcolor("#010989")
        t.pensize(3)
        # t.shape("tle")

        t.color("#bdbdbd")
        for rect in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(rect.x, rect.y)
            t.down()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.hideturtle()

        t.color("#010101")
        for sq in list_squares:
            t.showturle()
            t.up()
            t.goto(sq.x, sq.y)
            t.down()
            for i in range(2):
                t.forward(sq.width)
                t.left(90)
                t.forward(sq.height)
                t.left(90)
            t.hideturle()

        turtle.exitonclick()
