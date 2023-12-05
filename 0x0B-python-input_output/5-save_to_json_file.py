#!/usr/bin/python3
"""save_to_json_file module defines
"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file, using a JSON representation

    Args:
            my_obj (string): object represent json
            filename (string): the name of file to be write in
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
