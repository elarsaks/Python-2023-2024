#!/usr/bin/env python3

import numpy as np


def vector_angles(X, Y):
    # Calculate the inner products of corresponding vectors
    inner_products = np.einsum('ij,ij->i', X, Y)

    # Calculate the norms of the vectors in X and Y
    norms_X = np.linalg.norm(X, axis=1)
    norms_Y = np.linalg.norm(Y, axis=1)

    # Calculate the cosine of the angles
    cosines = inner_products / (norms_X * norms_Y)

    # Ensure the cosine values are in the valid range [-1.0, 1.0]
    cosines = np.clip(cosines, -1.0, 1.0)

    # Calculate the angles in radians and then convert to degrees
    angles = np.arccos(cosines)
    angles_degrees = np.degrees(angles)

    return angles_degrees


def main():
    # Example vectors in X and Y
    X = np.array([[1, 0], [0, 1], [1, 1]])
    Y = np.array([[0, 1], [1, 0], [1, 1]])

    # Get the angles
    angles = vector_angles(X, Y)
    print("Angles in degrees:", angles)


if __name__ == "__main__":
    main()
