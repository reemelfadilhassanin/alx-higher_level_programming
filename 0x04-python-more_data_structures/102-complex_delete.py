#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for x in list(a_dictionary.keys()):
        if a_dictionary[x] == value:
            a_dictionary.pop(x, None)
    return a_dictionary
