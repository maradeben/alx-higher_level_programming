#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ function to generate Pascal's triangle

    Args:
        n (int): the size of triangle

    Return:
        list of lists of integers representing Pascal triangle
            empty list if n <= 0
    """
    if (n <= 0):
        return ([])

    triangle = []
    for i in range(n):
        row = []
        if i == 0:
            # generate first row
            row = [0] * (n - 1)
            row.append(1)
        else:
            # generate other rows
            prev_row = triangle[i-1]
            tracker = len(prev_row) // 2
            row = [prev_row[j] + prev_row[j+1] for j in range(tracker)]

        if i % 2 == 0:
            row.extend(reversed(row[:-1]))
        else:
            row.extend(reversed(row[:]))

        triangle.append(row)

    # remove tracking 0's
    for row in triangle:
        while 0 in row:
            row.remove(0)

    return (triangle)
