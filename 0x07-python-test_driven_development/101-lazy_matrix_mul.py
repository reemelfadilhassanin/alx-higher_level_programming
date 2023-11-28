#!/usr/bin/python3
"""Defines a module lazy matrix multiplication using NumPy."""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Function to multibly m_a and m_b and return the multiplication of two matrices.

    Args:
            m_a (ints/floats): The first matrix.
            m_b (ints/floats): The second matrix.
    """

    return (numpy.matmul(m_a, m_b))
