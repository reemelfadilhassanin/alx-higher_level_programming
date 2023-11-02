#!/usr/bin/python3
if __name__ != "__main__":
    import sys
    exit()

argStr = "{:d} argument"
args = len(sys.argv) - 1
if args == 0:
   print("0 arguments.")
elif args == 1:
    print("1 argument:")
else:
    argStr += 's:'
print(argStr.format(args))

i = 0
for arg in sys.argv:
    if i != 0:
        print("{:d}: {:s}".format(i, arg))
    i += 1
