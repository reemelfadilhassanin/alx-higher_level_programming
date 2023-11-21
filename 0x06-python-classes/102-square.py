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

	@property
	def size(self):
		"""Retrive size.

		Returns:
			Value of size.
		"""
		return self.__size

	@size.setter
	def size(self, value):
		"""Setter method.

		Args:
			value (int): nust be int value.
		"""

		if not isinstance(value, int):
			raise TypeError("size must be an integer")
		elif value < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = value

	def area(self):
		"""Method cal the area of square.

		Returns: the square area.
		"""
		return self.__size ** 2

    def __lt__(self, other):
        """Rich comparison operator to compare if square area is less
        than another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false.
        """
        return self.__size < other.__size

    def __le__(self, other):
        """Method to compare squares.

        Args:
            other: square to compare.

        Returns: True or false.
        """
        return self.__size <= other.__size

    def __eq__(self, other):
        """Compare area of square.

        Args:
            other: square to compare.

        Returns: True or false
        """
        return self.__size == other.__size

    def __ne__(self, other):
        """Compare the equality value of area of squares.

        Args:
            other: square to compar.

        Returns: True or false
        """
        return self.__size != other.__size

    def __gt__(self, other):
        """Compare the area is greator.

        Args:
            other: square to compare.

        Returns: True or false
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """Check if area is >=.

        Args:
            other: square to compare.

        Returns: True or false
        """
        return self.__size >= ot
