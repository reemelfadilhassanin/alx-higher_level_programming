#!/usr/bin/python3
def max_integer(my_list=[]):
    size = len(my_list)
    if size:
        max = my_list[0]
        for item in my_list[1:]:
            max = max if item <= max else item
        return max
    else:
        return None
