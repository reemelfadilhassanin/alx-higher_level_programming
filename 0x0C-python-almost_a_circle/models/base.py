#!/usr/bin/python3
"""Defines a module for base class"""


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
