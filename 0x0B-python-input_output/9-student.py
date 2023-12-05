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

    def to_json(self):
        """ Puplic method that returns directory """
        return self.__dict__
