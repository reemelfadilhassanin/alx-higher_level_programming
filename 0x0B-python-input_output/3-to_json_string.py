#!/usr/bin/python3
"""
This is a to_json_string module.
"""

import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)

    Args:
            my_obj (string): string object want to seriliaze using json

    Returns:
            return: returns the JSON representation of an object
    """
    return json.dumps(my_obj)
