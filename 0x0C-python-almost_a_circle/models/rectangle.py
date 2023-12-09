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
        """Deines width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Define private attr of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Defines height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Define private attr of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Define private attr of rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Define private attr of rectangle"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Define private attr of rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Define private attr of rectangle"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
