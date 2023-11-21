#!/usr/bin/python3
"""class MagicClass"""
import math


class MagicClass:
    """
    Class that define MagicClass.

    Attributes:
        radius: radius.
    """
    def __init__(self, radius=0):
        """Construct initalize MagicClass.

        Args:
            radius: radius.

        Raises:
            TypeError: radius must be a number .
        """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """Print area

        Returns: retrive area.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Circumference

        Returns: retrive circumference.
        """
        return 2 * math.pi * self.__radius
