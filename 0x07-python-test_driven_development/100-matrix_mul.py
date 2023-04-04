#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """ Multiplies two matrices

    Argsuments:
        m_a (matrix): first matrix
        m_b (matrix): second matrix

    Raises:
        TypeError: if m_a or m_b is not a list
        TypeError: if either is not a list of lists
        ValueError: if either is empty
        TypeError: if any element in either is not int or float
        TypeError: if all rows in each is not of same size
        ValueError: if they can't be multiplied

    Returns:
        the resultant matrix
    """


    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(ele, list) for ele in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(ele, list) for ele in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all([all([type(i) == float or type(i) == int for i in ele])\
        for ele in m_a]):
            raise TypeError("m_a should contain integers or floats")
    if not all([all([type(i) == float or type(i) == int for i in ele])\
        for ele in m_b]):
            raise TypeError("m_b should contain integers or floats")
    if not all(len(m_a[0]) == len(ele) for ele in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(ele) for ele in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    result = []

    for row in m_a:
        res_row = []
        for b_t in range(len(m_b[0])):
            col = [col[b_t] for col in m_b]
            value = sum(row[i] * col[i] for i in range(len(row)))
            res_row.append(value)
        result.append(res_row)

    return result
