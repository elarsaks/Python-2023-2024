#!/usr/bin/env python3

import numpy as np


def multiplication_table(n):
    # Create an array of values from 0 to n-1
    values = np.arange(n)

    # Reshape values to a column vector for broadcasting
    column_values = values.reshape(n, 1)

    # Use broadcasting to multiply column vector with row vector (values)
    table = column_values * values

    return table


def main():
    print(multiplication_table(4))


if __name__ == "__main__":
    main()
