#!/usr/bin/python3
""" Deine Student module
"""


class Student:
    """ a class Student that defines a student """

    def __init__(self, first_name, last_name, age):
        """ constructor to initilize objects of student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Puplic method that returns directory """
        if (type(attrs) == list and
                all(type(x) == str for x in attrs)):
            return {s: getattr(self, s) for s in attrs if hasattr(self, s)}
        return self.__dict__

    def reload_from_json(self, json):
        """Method to replace all attributes of the Student.
        Args:
                json (dict): dictionary.
        """
        for a in json:
            self.__dict__[a] = json[a]
