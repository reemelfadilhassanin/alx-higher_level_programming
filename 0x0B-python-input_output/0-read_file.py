#!/usr/bin/python3
"""
Define Read file module
"""


def read_file(filename=""):
    """_summary_

    Args:
            filename (str, optional): text file to be read
    """

    with open(filename, "r", encoding="utf-8") as f:
        data_read = f.read()
        print(data_read, end="")
