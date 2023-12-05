#!/usr/bin/python3
"""
Define write file module
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)

    Args:
            filename (str, optional): file name"".
            text (str, optional): text to be write in file "".

    Returns:
            Return: returns the number of characters written
    """
    with open(filename, 'w') as f:
        write_test = f.write(text)
        return write_test
