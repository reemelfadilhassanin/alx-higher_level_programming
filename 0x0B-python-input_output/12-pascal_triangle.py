#!/usr/bin/python3
"""This Pascal's Triangle module."""


def pascal_triangle(n):
    """Method to returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    tr = [[1]]
    while len(tr) != n:
        x = tr[-1]
        tm = [1]
        for i in range(len(x) - 1):
            tm.append(x[i] + x[i + 1])
        tm.append(1)
        tr.append(tm)
    return tr
