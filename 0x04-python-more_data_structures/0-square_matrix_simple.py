#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    # make a copy to avoid modifying original
    squared = [row for row in matrix]
    squared = [list(map(lambda x:x**2, row)) for row in matrix]
    return squared
