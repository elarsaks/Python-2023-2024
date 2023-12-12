#!/usr/bin/python3

import numpy as np


def almost_meeting_lines(a1, b1, a2, b2):
    A = np.array([[a1, b1], [a2, b2]])
    B = np.array([1, 1])

    # Check if lines are parallel (determinant is zero or close to zero)
    if np.isclose(np.linalg.det(A), 0):
        # Use least squares to find the closest point
        result = np.linalg.lstsq(A, B, rcond=None)
        point = result[0]
        return (point[0], point[1]), False
    else:
        # Lines are not parallel, solve normally
        point = np.linalg.solve(A, B)
        return (point[0], point[1]), True


def main():
    a1, b1, a2, b2 = 1, 2, -1, 0
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    print(x, y, exact)

    # Additional test cases
    a1, b1, a2, b2 = 1, 2, 1, -2
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    print(f"Closest point at x={x} and y={y}, exact={exact}")

    a1, b1, a2, b2 = 1, 2, 1, 2
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    print(f"Closest point at x={x} and y={y}, exact={exact}")

    a1, b1, a2, b2 = 1, 2, 1, 1
    (x, y), exact = almost_meeting_lines(a1, b1, a2, b2)
    print(f"Closest point at x={x} and y={y}, exact={exact}")


if __name__ == "__main__":
    main()
