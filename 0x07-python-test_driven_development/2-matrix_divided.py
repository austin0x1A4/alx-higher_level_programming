#!/usr/bin/python3
"""Divides all elements of a matrix

Prototype: def matrix_divided(matrix, div):
- matrix must be a list of lists of integers/floats, otherwise raise a TypeError
exception with the message matrix must be a matrix (list of lists) of integers/floats
- Each row of the matrix must have the same size, otherwise raise a TypeError 
exception with the message Each row of the matrix must have the same size
- div must be a number (integer or float), otherwise raise a TypeError
exception with the message div must be a number
- div can't be equal to 0, otherwise raise a ZeroDivisionError
exception with the message division by zero
- All elements of the matrix should be divided by div, rounded to 2 decimal places  
- Returns a new matrix
"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix: list of lists of ints/floats
        div: number to divide matrix by
    
    Returns:
        new matrix with result

    Raises:
        TypeError: if matrix is not a list of lists, div is not a number
        ZeroDivisionError: if div is 0
    """

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
