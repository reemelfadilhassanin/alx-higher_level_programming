#!/usr/bin/python3
""" Define from_json_string module
"""

import json


def from_json_string(my_str):
    """ function that returns an object represented by a JSON string

    Args:
            my_str (str): object (Python data structure) want to deserilize

    Returns:
            Return: returns an Python data structure dectionary
    """
    return json.loads(my_str)
