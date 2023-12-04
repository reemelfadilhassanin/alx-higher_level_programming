#!/usr/bin/python3
"""define function that add new attribute
"""


def add_attribute(ob, attr, val):
    """define function that add new attribute"""
    if '__dict__' not in dir(ob):
        raise TypeError("can't add new attribute")
    if '__slots__' in dir(ob):
        raise TypeError("can't add new attribute")
    else:
        setattr(ob, attr, val)
