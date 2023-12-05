#!/usr/bin/python3
""" Define load_from_json_file module
"""
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file

    Args:
        filename: the name of textfile

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
