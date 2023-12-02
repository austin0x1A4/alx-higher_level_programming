#!/usr/bin/python3
"""Multiplies two matrices
Prototype: def matrix_mul(m_a, m_b):
- m_a and m_b must be validated as:
  - lists of lists of ints/floats
  - same size rows 
  - not empty
- Raises:
  - TypeError if invalid types
  - ValueError if incompatible for multiplication
"""

def matrix_mul(m_a, m_b):
    """Multiply two matrices

    Args:
        m_a: first matrix 
        m_b: second matrix

    Raises:
        TypeError: if invalid matrix type
        ValueError: if incompatible dimensions

    Returns:
        New matrix representing product of m_a * m_b
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

    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    result = [[sum(a*b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result
