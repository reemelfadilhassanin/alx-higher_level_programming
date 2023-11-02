#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

count = "{:d} argument"
args = len(sys.argv) - 1
if args == 0:
    count += 's.'
elif args == 1:
    count += ':'
else:
    count += 's:'
print(count.format(args))

i = 0
for arg in sys.argv:
    if i != 0:
        print("{}: {}".format(i, arg))
    i += 1
