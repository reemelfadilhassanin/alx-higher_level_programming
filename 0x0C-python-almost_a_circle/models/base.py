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
