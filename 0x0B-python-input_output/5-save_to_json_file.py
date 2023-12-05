#!/usr/bin/python3
""" Define save_to_json_file module
"""
import json


def save_to_json_file(my_obj, filename):
    """ Define function that writes an object to a text file
    by a JSON representation

    Args:
        my_obj: object
        filename: the name of text file

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
