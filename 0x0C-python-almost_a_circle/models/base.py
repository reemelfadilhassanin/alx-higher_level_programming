#!/usr/bin/python3
"""Defines a module for base class"""
import json
from json import dumps, loads
import csv
import turtle


class Base:
    """Class to manage id attribute in"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor initializing object id"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method return JSON serialization of list dic.

        Args:
            list_dictionaries (list): list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        if list_dictionaries is list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string format of list_objs to a file.

        Args:
            list_objs (list): A list instanse of inherited Base class.
        """

        f_joson = "{}.json".format(cls.__name__)
        json_list = []
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open(f_joson, "w", encoding="utf-8") as f2:
            if list_objs is None:
                f2.write("[]")
            else:
                f2.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Define static method.

        Args:
            json_string (str): Astring representing a list of dictionaries
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - return list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Define create module

        Returns:
            return: instance with all attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == Rectangle:
            dummy = Rectangle(1, 1)
        elif cls.__name__ == Square:
            dummy = Square(1)
        else:
            dummy = None
        if dummy:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Define class method load_from_file.
        Returns:
            Empty list - If the file does not exist.
            Otherwise - a list of instantiated classes.
        """
        file1 = str(cls.__name__) + ".json"
        try:
            with open(file1, "r") as file2:
                list_dicts = Base.from_json_string(file2.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Define module that loads and dumps in CSV.
        """
        file1 = cls.__name__ + ".csv"
        with open(file1, "w", newline="", encoding='utf-8') as file2:
            if list_objs is None or list_objs == []:
                file2.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    obs = ["id", "width", "height", "x", "y"]
                else:
                    obs = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file2, fieldnames=obs)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Define this module.
        """

        file1 = cls.__name__ + ".csv"
        try:
            with open(file1, "r", newline="") as x:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(x, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Defines this module.
        Args:
            list_rectangles (list): list of Rectangle to draw.
            list_squares (list): list of Square to draw.
        """
        tu = turtle.Turtle()
        tu.screen.bgcolor("#b7312c")
        tu.pensize(3)
        tu.shape("turtle")

        tu.color("#ffffff")
        for rect in list_rectangles:
            tu.showturtle()
            tu.up()
            tu.goto(rect.x, rect.y)
            tu.down()
            for i in range(2):
                tu.forward(rect.width)
                tu.left(90)
                tu.forward(rect.height)
                tu.left(90)
            tu.hideturtle()

        tu.color("#b5e3d8")
        for sq in list_squares:
            tu.showturtle()
            tu.up()
            tu.goto(sq.x, sq.y)
            tu.down()
            for i in range(2):
                tu.forward(sq.width)
                tu.left(90)
                tu.forward(sq.height)
                tu.left(90)
            tu.hideturtle()

        tu.exitonclick()
