#!/usr/bin/python3
""" This append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file

    Args:
        filename: the name of file to be appended
        search_string: the string wanted to found
        new_string: the new string to be appende

    """

    readbuff = []
    with open(filename, 'r', encoding="utf-8") as f:
        for buff in f:
            readbuff += [buff]
            if buff.find(search_string) != -1:
                readbuff += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(readbuff))
