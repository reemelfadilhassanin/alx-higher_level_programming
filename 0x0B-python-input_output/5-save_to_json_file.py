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
        str_json = json.dumps(my_obj)
        f.write(str_json)
