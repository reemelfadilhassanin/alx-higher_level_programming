#!/usr/bin/python3
"""Define append_write module"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8).
    Args:
        filename (str): define the name of file to be apppended.
        text (str): the text string to be append to file.
    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        add_test = f.write(text)
        return add_test
