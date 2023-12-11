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

    def update(self, *args, **kwargs):
        """Define update the Square module.

        Args:
        *args (ints): New arrguments values.
        - 1 argument represents id attribute
        - 2 argument represents size attribute
        - 3 argument represents x attribute
        - 4 argument represents y attribute
        **kwargs (dict): New key/value pairs of attributes.
        """

        if args:
            for i in range(len(args)):
                if i == 0:
                    if type(args[i]) is not int:
                        raise TypeError("id must be an integer")
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) is not int:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary information of a square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
