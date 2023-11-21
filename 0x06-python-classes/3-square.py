#!/usr/bin/python3
"""This define square class"""


class Square:
	"""
	Class has no attribute and construct have none.

	Args:
		size: private instance size of the square.
	"""
	def __init__(self, size=0):
		"""Constructor of square with one instance size.

		Args:
		   size: private instance size of the square.
		"""
		self.__size = size

		if not isinstance(size, int):
			raise TypeError("size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = size
	
	def area(self):
		"""Public method of the area.

		Returns: method return current area.
		"""
		return self.__size ** 2
