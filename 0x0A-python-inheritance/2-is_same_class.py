#!/usr/bin/python3
"""Defines a is_same_class module."""


def is_same_class(obj, a_class):
    """Method thatcheck if an object is exactly an instance of a given class.
    Args:
        obj (any): The object to check.
        a_class (type): class to check.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    return (type(obj) == a_class)
