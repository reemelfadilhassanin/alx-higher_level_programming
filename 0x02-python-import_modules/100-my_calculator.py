#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ != "__main__":
    exit()

if len(argv) != 4:
      print("Usage: ./100-my_calculator.py <a> <operator> <b>")  
      exit(1)
      a = int(argv[1])
      op = argv[2]
      b = int(argv[3])

      if op == '+':
        print("{} + {} = {}".format(a,b, add(a,b)))
      elif op == '-':
        print("{} - {} = {}".format(a,b, sub(a,b)))
      elif op == '*':
        print("{} * {} = {}".format(a,b, mul(a,b)))
      elif op == '/':
        print("{} / {} = {}".format(a,b, div(a,b)))
      else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
