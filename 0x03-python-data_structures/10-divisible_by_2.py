#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []
    for i in my_list:
        list.append(i % 2 == 0)
    return list
