#!/usr/bin/python3
"""This defines a Rectangle class."""


class Rectangle:
    """This represent a rectangle class."""

    def __init__(self, width=0, height=0):
        """Constructor of new object Rectangle.
        Args:
            width (int): The width of rectangle.
            height (int): The height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """public instance method to set width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Public inst method to set height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """Print the rectangle with the character #.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            [rect_str.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect_str.append("\n")
        return ("".join(rect_str))

    def __repr__(self):
        """Return a string representation of the rectangle"""

        return f"Rectangle({self.__width}, {self.__height})"


def __del__(self):
    """Print the message Bye rectangle...
    """


print("Bye rectangle...")


def perimeter(self):
    """public instance to return the perimeter of the Rectangle."""
    if self.__width == 0 or self.__height == 0:
        return (0)
    return ((self.__width * 2) + (self.__height * 2))
