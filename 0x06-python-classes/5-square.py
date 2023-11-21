#!/usr/bin/python3
"""This define square class"""


class Square:
    """
    Class has no attribute and construct have none.

    Attributes:
         size: private instance size of the square.
    """
    def __init__(self, size=0):
        """Constructor of square with one instance size.

        Args:
           size: private instance size of the square.
		"""
        self.__size = size

    def area(self):
        """Method cal the area of square.

       Returns: the square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method.

        Args:
            value (int): nust be int value..

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints # in  square
        """

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))
