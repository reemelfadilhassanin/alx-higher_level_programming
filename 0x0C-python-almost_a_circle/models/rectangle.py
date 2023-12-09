#!/usr/bin/python3
"""Defines a module for rectangle class"""
import json
from models.base import Base


class Rectangle(Base):
    """Deine rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor to initializing ob of class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Define width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Protect witdth of the rectangle"""
        self.__width = value

    @property
    def height(self):
        """Define height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the height of the rectangle"""
        self.__height = value

    @property
    def x(self):
        """The x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Define private attr of rectangle"""
        self.__x = value

    @property
    def y(self):
        """Define private attr of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Define private attr of rectangle"""

        self.__y = value
