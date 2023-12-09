#!/usr/bin/env python3

import numpy as np


def vector_lengths(a):
    # Calculate the squared values of all elements
    squared_elements = np.square(a)

    # Sum the squares along each row (axis=1)
    sum_of_squares = np.sum(squared_elements, axis=1)

    # Take the square root of the sum of squares
    lengths = np.sqrt(sum_of_squares)

    return lengths


def main():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Input array:\n", a)
    print("Lengths of vectors:", vector_lengths(a))


if __name__ == "__main__":
    main()
