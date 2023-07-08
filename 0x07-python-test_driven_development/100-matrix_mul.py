#!/usr/bin/python3
"""
module for matrix multiplication
"""

def matrix_mul(m_a, m_b):
    """
    function that multiplies two matrices

    Args:
        m_a (list): list of list of integers or floats
        m_b (list): list of list of integers or floats
    
        Raises:
            TypeError: if m_a or m_b is not a list or list of list
            ValueError: if m_a or m_b is empty
            TypeError: if m_a or m_b does not contain only integers or floats
            TypeError: if each row of m_a or m_b are not the same
            ValueError: if m_a and m_b cannot be multiplied
        
            Returns:
                (list): product of m_a and m_b
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(e, int) or isinstance(e, float)
               for e in [i for row in m_a for i in row]):
        raise TypeError("m_a should contain only integer or floats")
    if not all(isinstance(e, int) or isinstance(e, float)
               for e in [i for row in m_b for i in row]):
        raise TypeError("m_b should contain only integer or floats")
    max_size = max(len(r) for r in m_a)
    if not all(len(r) == max_size for r in m_a):
        raise TypeError("each row fo m_a must be of the same size")
    max_size = max(len(r) for r in m_b)
    if not all(len(r) == max_size for r in m_b):
        raise TypeError("each row fo m_b must be of the same size")
    if not len(m_a[0]) == len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    m_a_times_m_b = [[0, ] * len(m_b[0]) for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_a_times_m_b[i][j] += m_a[i][k] * m_b[k][j]
    return m_a_times_m_b
