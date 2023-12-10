#!/usr/bin/python3
"""Defines module for square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines square class inharit from rectangle

    Args:
                    Rectangle:supper class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """constructor for initialize object of class

        Args:
                        size (int): size of square
                        x (int): x coordinate of square. Defaults to 0.
                        y (int): y coordinate of square. Defaults to 0.
                        id (int): id of square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Define string module for square.

        Returns:
                        return: return string format for square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,  self.y, self.width)

    @property
    def size(self):
        """Module for getting size of Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Module for setting size of Square."""
        self.width = value
        self.height = value
