#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    for i in range(x):
        try:
            x = my_list[i]
            if type(x) == int:
                print("{:d}".format(x), end='')
                index = index + 1
        except (ValueError, TypeError):
            pass
    print()
    return index
