#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    i = 0

    try:
        for i in range(0, x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                index = index + 1
    except IndexError:
        pass
    finally:
        print()
        return index
