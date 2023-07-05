#!/usr/bin/python3
"""
matrix division module
"""


def matrix_divided(matrix, div):
    """Return a new matrix with the results of element wise division

    Args:
        matrix (list): a matrix
        div (integer or float): divisor

    Raises:
        TypeError: if the matrix contains non-numbers
        TypeError: if the matrix contains rows of different sizes
        TypeError: if the div is not an integer or float
        ZeroDivisionError: if div is zero

    Returns:
        (list): new matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(e, int) or isinstance(e, float) for e in
            [i for row in matrix for i in row])):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda e: round(e / div, 2), row)) for row in matrix]
