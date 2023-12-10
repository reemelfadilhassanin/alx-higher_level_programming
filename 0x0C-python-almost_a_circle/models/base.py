#!/usr/bin/python3
"""Defines a module for base class"""
import json
from json import dumps, loads


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
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy
