#!/usr/bin/python3
"""Matrix Division module"""


def matrix_divided(matrix, div):
    """A function to divide all elements of a matrix by
        a sngle number

    Arguments:
        matrix (list of lists): the matrix of numbers
        div (int or float): the divisor

    Raises:
        TypeError: if matrix is not a list of integers or floats
            or if each row of the matrix is not of the same size
            or if div is not an integer or a float
        ZeroDivisionError: if div is 0

    Returns:
        result matrix with all results to 2 decimal places
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if len(set([len(item) for item in matrix])) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
