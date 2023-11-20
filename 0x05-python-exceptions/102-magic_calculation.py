#!/usr/bin/python3
def magic_calculation(a, b):
    count = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception("Too far")
            count += (a ** b) / x
        except Exception:
            count = b + a
            break
    return count
