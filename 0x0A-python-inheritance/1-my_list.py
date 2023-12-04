#!/usr/bin/python3
"""
MyList class inharit list class
"""


class MyList(list):
    """a driveclass from class list"""

    def __init__(self):
        """Costruct initalize object"""
        super().__init__()

    def print_sorted(self):
        """prints list in sorte way"""
        print(sorted(self))
