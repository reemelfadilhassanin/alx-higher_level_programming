#!/usr/bin/python3
def uppercase(str):
    for u in range(len(str)):
        char = ord(str[u])
        if char >= 97 and char <= 122:
            char = char - 32
        print("{}".format(chr(char)), end="")
    print()
