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
        if type(value) != int:
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
        if type(value) != int:
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
        if type(value) != int:
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

    def area(self):
        """Define public methof of rectangle

        Returns:
                                                                                                                                        Return: return the area
        """
        return self.width * self.height

    def display(self):
        """Defines puplic method to printe rectangle in stdout"""
        dis = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(dis, end='')

    def __str__(self):
        """Overriding the __str__ method
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Define update method"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    if type(args[i]) is not int:
                        raise TypeError("id must be an integer")
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) is not int:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary information of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
