#!/usr/bin/env python3

import numpy as np


def diamond(n):
    # Create an identity matrix of size n
    identity_matrix = np.eye(n, dtype=int)

    # Create the upper half of the diamond
    upper_half = np.concatenate(
        (np.flip(identity_matrix, axis=1), identity_matrix[:, 1:]), axis=1)

    # Create the lower half of the diamond
    lower_half = np.concatenate(
        (identity_matrix, np.flip(identity_matrix, axis=1)[:, 1:]), axis=1)

    # Concatenate the upper and lower halves
    diamond_shape = np.concatenate((upper_half, lower_half[1:]), axis=0)

    return diamond_shape


def main():
    n = 5  # Example side length
    diamond_shape = diamond(n)
    print(diamond_shape)


if __name__ == "__main__":
    main()
