#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    
    sum_weight = sum(a * b for a, b in my_list)
    total = sum(b for a, b in my_list)

    return sum_weight / total if total != 0 else 0
