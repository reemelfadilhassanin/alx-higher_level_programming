#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    else:
     if sum(b for a, b in my_list) != 0:
        return (sum(a * b for a, b in my_list) / sum(b for a, b in my_list))
     else:
           return 0
