#!/usr/bin/python3
"""
Define module BaseGeometry
"""


class BaseGeometry:
    """Dfine Public instance method area"""

    def area(self):
        """raises exception if not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Dfine Public instance method integer_validator """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
