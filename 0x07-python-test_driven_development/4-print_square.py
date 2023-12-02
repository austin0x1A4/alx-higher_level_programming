#!/usr/bin/python3
"""Prints a square with the # character. 

Prototype: def print_square(size):
- size is the size length of the square
- size must be an integer, otherwise raise a TypeError exception with the message 
  size must be an integer
- if size is less than 0, raise a ValueError exception with the message 
  size must be >= 0 
- if size is a float and is less than 0, raise a TypeError
- You are not allowed to import any module
"""

def print_square(size):
    """Print a square with the # character.

    Args:
        size: length of the square

    Raises:
        TypeError: if size is not an integer 
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        print("#" * size)
