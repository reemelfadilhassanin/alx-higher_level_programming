#!/usr/bin/python3
""" Define save_to_json_file module
"""

import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file, using a JSON representation

    Args:
            my_obj (str): object (Python data structure) want to deserilize
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
