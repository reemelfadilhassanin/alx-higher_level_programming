#!/usr/bin/python3
"""This define square class"""


class Square:
    """Class has no attribute and construct have none.
    """
    def __init__(self, size = 0):
        """Constructor of square with one instance size.

        Args:
            size: private instance size of the square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is > 0.
        """
        self.__size = size
        
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
