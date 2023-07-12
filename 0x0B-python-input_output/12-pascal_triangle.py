#!/usr/bin/python3
"""
module to build a pascal triangle
"""


def pascal_triangle(n):
    """
    Appends each row of Pascal's triangle up to order n to a list

    Args:
        n (integer): order of triangle

    Returns:
        (list of lists)
    """
    triangle = []  # Initialize an empty list to store the rows

    for i in range(1, n + 1):
        row = generate_row(i)  # Generate the row for the current value of n
        triangle.append(row)  # Append the row to the triangle list

    return triangle


def generate_row(n):
    """
    Generates a single row of Pascal's triangle

    Args:
        n (integer): order of the row

    Returns:
        (list)
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    previous_row = generate_row(n - 1)  # Generate the previous row
    row = [1] + summing(previous_row) + [1]  # Generate the current row
    return row


def summing(lst):
    """
    Sums two consecutive elements in a list and returns a new list

    Args:
        lst (list): list of integers

    Returns:
        (list)
    """
    return [sum(lst[i:i + 2]) for i in range(len(lst) - 1)]
