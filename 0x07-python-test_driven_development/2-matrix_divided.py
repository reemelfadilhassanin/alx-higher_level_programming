#!/usr/bin/python3
"""This module for matrix_divided method."""


def matrix_divided(matrix, div):
    """Using div to divide all elements of matrix.
    Args:
            matrix(list): List of int or float
            div: int/float number to divide matrix
    Returns:
            list: List of new divided matrix.
    Raises:
            TypeError: If matrix is not list of int or float.
            TypeError: If submatrix are not all same size.
            TypeError: If div is not int or float.
            ZeroDivisionError: If div is zero.
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError(error)
    if len(matrix) == 0:
        raise TypeError(error)
    for lis in matrix:
        if not isinstance(lis, list) or len(lis) == 0:
            raise TypeError(error)
        if len(lis) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in lis:
            if not isinstance(x, (int, float)):
                raise TypeError(error)
    return [[round(x / div, 2) for x in lis] for lis in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
