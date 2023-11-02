#!/usr/bin/python3
import sys
import hidden_4 as hidden

if __name__ != "__main__":
    exit()

for i in dir(hidden):
    if i[:2] != "__":
        print(i)
