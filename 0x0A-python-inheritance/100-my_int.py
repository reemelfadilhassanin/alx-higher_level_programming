#!/usr/bin/python3
"""
This module MyInt
"""


class MyInt(int):
    """Define MyInt rebel version of an integer"""

    def __eq__(self, label):
        """override operan !="""
        return int(self) != label

    def __ne__(self, label):
        """override operand =="""
        return int(self) == label
