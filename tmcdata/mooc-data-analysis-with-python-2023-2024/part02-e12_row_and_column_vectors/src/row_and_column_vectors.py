#!/usr/bin/env python3

import numpy as np


def get_row_vectors(a):
    # Create a list of row vectors from the array 'a'
    # Each row vector is extracted with a new axis to make its shape (1, m)
    return [a[i, np.newaxis, :] for i in range(a.shape[0])]


def get_column_vectors(a):
    # Create a list of column vectors from the array 'a'
    # Each column vector is extracted with a new axis to make its shape (n, 1)
    return [a[:, i, np.newaxis] for i in range(a.shape[1])]


def main():
    # Set a seed for the random number generator for reproducibility
    np.random.seed(0)

    # Generate a 4x4 array of random integers between 0 and 9
    a = np.random.randint(0, 10, (4, 4))

    # Print the generated array
    print("a:", a)

    # Print the row vectors of the array
    print("Row vectors:", get_row_vectors(a))

    # Print the column vectors of the array
    print("Column vectors:", get_column_vectors(a))


if __name__ == "__main__":
    main()
