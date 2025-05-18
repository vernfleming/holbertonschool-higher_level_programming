#!/usr/bin/python3
"""Module that divides all elements of a matrix by a number."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.
    Returns a new matrix with results rounded to 2 decimal places.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or
    not all(isinstance(row, list) for row in matrix):
        raise TypeError(err)

    if not all(
        isinstance(x, (int, float)) for row in matrix for x in row
    ):
        raise TypeError(err)

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(x / div, 2) for x in row]
        for row in matrix
    ]
