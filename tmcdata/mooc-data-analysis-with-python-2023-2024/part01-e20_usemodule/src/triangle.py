"""
triangle_math module

This module provides functions to calculate properties of a right-angled triangle.
"""

__version__ = "1.0"
__author__ = "Your Name"

import math


def hypotenuse(side1, side2):
    """
    Calculate the length of the hypotenuse in a right-angled triangle.

    Parameters:
    side1 (float): Length of one side of the triangle.
    side2 (float): Length of the other side of the triangle.

    Returns:
    float: Length of the hypotenuse.
    """
    return math.sqrt(side1**2 + side2**2)


def area(side1, side2):
    """
    Calculate the area of a right-angled triangle.

    Parameters:
    side1 (float): Length of one side of the triangle.
    side2 (float): Length of the other side of the triangle.

    Returns:
    float: Area of the triangle.
    """
    return 0.5 * side1 * side2
