#!/usr/bin/python3
"""
module for lazy matrix multiplication
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    product of two matrices using numpy library

    Args:
        m_a (list): first matrix
        m_b (list): second matrix
    
    Returns:
        (list): product of m_a and m_b
    """
    return np.matmul(m_a, m_b).tolist()
