#!/usr/bin/python3
"""
Define class Rectangle
"""


class BaseGeometry:
    """Dfine Public instance method area"""

    def area(self):
        """raises exception if not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dfine Public instance method integer_validator"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Define class Rectangle"""

    def __init__(self, width, height):
        """define constructor"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return representation of the rectangle"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))


class Square(Rectangle):
    """define Square class"""

    def __init__(self, size):
        """define constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"define area of squre"""
        return self.__size ** 2

    def __str__(self):
        """return reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
