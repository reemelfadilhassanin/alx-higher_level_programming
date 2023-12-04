#!/usr/bin/python3
"""
Define class Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """define constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
