#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in range(len(matrix)):
        result += [list(map(lambda x: x * x, matrix[i]))]
    return result
