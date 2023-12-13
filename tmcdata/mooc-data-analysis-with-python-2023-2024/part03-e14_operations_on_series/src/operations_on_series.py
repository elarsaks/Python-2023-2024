#!/usr/bin/env python3

import pandas as pd


def create_series(L1, L2):
    """
    Create two Series from two lists with indices 'a', 'b', and 'c'.

    Parameters:
    L1 (list): A list of numbers for the first Series.
    L2 (list): A list of numbers for the second Series.

    Returns:
    tuple: A tuple containing the two created Series.
    """
    if len(L1) != 3 or len(L2) != 3:
        raise ValueError("Both lists should have length 3.")

    indices = ['a', 'b', 'c']
    s1 = pd.Series(L1, index=indices)
    s2 = pd.Series(L2, index=indices)
    return s1, s2


def modify_series(s1, s2):
    """
    Modify the first Series by adding a new value with index 'd', which is the same as the value in the second Series with index 'b'.
    Then delete the element with index 'b' from the second Series.

    Parameters:
    s1 (pd.Series): The first Series.
    s2 (pd.Series): The second Series.

    Returns:
    tuple: A tuple containing the modified Series.
    """
    s1['d'] = s2['b']
    del s2['b']
    return s1, s2


def main():
    # Test the functions
    L1 = [1, 2, 3]
    L2 = [4, 5, 6]

    s1, s2 = create_series(L1, L2)
    print("Original Series:")
    print("s1:\n", s1)
    print("s2:\n", s2)

    s1, s2 = modify_series(s1, s2)
    print("\nModified Series:")
    print("s1:\n", s1)
    print("s2:\n", s2)

    print("\nSum of Series:")
    print(s1 + s2)


if __name__ == "__main__":
    main()
