#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiply 2 matrices using NumPy

    Args:
        m_a: first matrix
        m_b: second matrix
    
    Returns:
        Product of m_a and m_b
    """

    try:
        return np.matmul(m_a, m_b)
    except Exception as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
