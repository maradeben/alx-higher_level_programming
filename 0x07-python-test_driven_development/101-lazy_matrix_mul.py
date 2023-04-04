#!/usr/bin/python3
"""Lazy matrix multiplication with numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Matrix multiplication with numpy
    
    Arguments:
        m_a (matrix): matrix one
        m_b (matrix): matrix two

    Returns:
        the result
    """

    return (np.matmul(m_a, m_b))
