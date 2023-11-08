#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    else:
        return (sum(a * b for a, b in my_list) / sum(b for a, b in my_list) if sum(b for a, b in my_list) != 0 else 0)
