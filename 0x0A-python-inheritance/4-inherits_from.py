#!/usr/bin/python3
"""4-inherits_from.py"""


def inherits_from(obj, a_class):
    """Check the object is an instance of a class that inherited

    Args:
            obj: object to be inherert
            a_class: class to be inheret

    Returns:
            return: true if the check is valid , otherwise False
    """
    return type(obj) != a_class and isinstance(obj, a_class)
