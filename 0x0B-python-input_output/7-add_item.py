#!/usr/bin/python3
"""this module add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        x = load_from_json_file("add_item.json")
    except FileNotFoundError:
        x = []
    x.extend(sys.argv[1:])
    save_to_json_file(x, "add_item.json")
