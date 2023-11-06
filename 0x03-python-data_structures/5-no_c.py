#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for s in my_string:
        if s != 'c' and s != 'C':
         new_string += s
    return new_string
