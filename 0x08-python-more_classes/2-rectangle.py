#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Define rectangle with public and private instance."""

    def __init__(self, width=0, height=0):
        """Constructor initialize a new object Rectangle.
        Args:
            width (int): The width of rectangle.
            height (int): The height of rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Define private  instance width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Get the width private value 

        Attributes:
                value (int): int value for width of rectangle

        Raises:
                TypeError: If `value` is not an int.
                ValueError: If `value` is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Define public attribuite area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Define Public instance method that return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)
