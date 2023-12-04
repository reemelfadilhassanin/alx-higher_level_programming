#!/usr/bin/python3
"""
dfine Square odule
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define Square class"""

    def __init__(self, size):
        """define constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
