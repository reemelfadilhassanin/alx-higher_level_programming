#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except Exception as e:
        result = None
    else:
        print("Inside result: {}".format(result))
        return result
