#!/usr/bin/env python3
import numpy as np
from functools import reduce


def matrix_power(a, n):
    # Handle the case when n is 0
    if n == 0:
        return np.eye(a.shape[0])

    # Handle negative powers
    if n < 0:
        a = np.linalg.inv(a)
        n = -n

    # Use reduce to perform repeated matrix multiplication
    return reduce(np.matmul, (a for _ in range(n)))


def main():
    a = np.array([[1, 2], [3, 4]])
    print(matrix_power(a, 2))  # Should print the matrix a multiplied by itself
    print(matrix_power(a, -1))  # Should print the inverse of matrix a
    return


if __name__ == "__main__":
    main()
