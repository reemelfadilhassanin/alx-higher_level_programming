#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
         return None
    else:
        max = my_list[0]
        for i in my_list[1:]:
            max = max if i <= max else i
        return max
