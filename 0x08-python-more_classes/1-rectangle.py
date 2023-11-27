#!/usr/bin/python3
"""This define Rectangle class"""


class Rectangle:
    """Define recyangle class with private attribute.
    Attributes:
    __height (float): height of rectangle.
    __width (float): Width of rectangle."""

    def __init__(self, width=0, height=0):
        """create contstructor object 

        Args:
                width (int, optional): integer width. Defaults to 0.
                height (int, optional): int hight. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter private value.

        Returns:
                __width (int): width private value

        """
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
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get the height for private attribute of rectangle.

        Returns:
                __height (int): hight with private of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """set the value for hight.

        Args:
                value (int): int value for hight of rectangle

        Attributes:
                __height (int): hight of rectangle

        Raises:
                TypeError: If `value` is not an int.
                ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
