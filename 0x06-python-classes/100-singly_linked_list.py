#!/usr/bin/python3
"""Defines the classes of SinglyLinkedList"""


class Node:
	"""
	Class Node.

	Attributes:
		data: data of node.
	"""
	def __init__(self, data, next_node=None):
		"""Creates constructor of node.

		Args:
			__data : data field of linklist.
		"""
		self.data = data
		self.next_node = next_node

	@property
	def data(self):
		"""Getter method.

		Returns: int value of data field.
		"""
		return self.__data

	@data.setter
	def data(self, value):
		"""Method of setter for data.

		Args:
			value: int value for data field.

		Raises:
			TypeError: if is not an integer
		"""
		if not isinstance(value, int):
			raise TypeError("data must be an integer")
		self.__data = value

	@property
	def next_node(self):
		"""Gette method for the next_node instance.

		Returns: Value of next_node instance.
		"""
		return self.__next_node

	@next_node.setter
	def next_node(self, value):
		"""Method setter for Node.

		Args:
			value (None): next node of a Node.

		Raises:
			TypeError: next_node must be a Node object .
		"""
		if value is not None and not isinstance(value, Node):
			raise TypeError("next_node must be a Node object")
		self.__next_node = value


class SinglyLinkedList:
	"""
	Class of SinglyLinkedList.

	Attributes:
		head: head of the SinglyLinkedList.
	"""
	def __init__(self):
		"""Construction of SinglyLinkedList .

		Args:
			__head : head of the SinglyLinkedList .
		"""
		self.__head = None

	def __str__(self):
		"""Class objects as a string.

		Returns: The class object.
		"""
		temp_var = self.__head
		print_node = []
		while temp_var:
			print_node.sort()
			print_node.append(str(temp_var.data))
			temp_var = temp_var.next_node

		print_node.sort(key=int)
		return ("\n".join(print_node))

	def sorted_insert(self, value):
		"""Inserts a new node .

		Args:
			value: value.
		"""
		if self.__head is None:
			new_node = Node(value)
			new_node.next_node = self.__head
			self.__head = new_node
		else:
			new_node = Node(value)
			new_node.data = value
			new_node.next_node = self.__head
			self.__head = new_node
