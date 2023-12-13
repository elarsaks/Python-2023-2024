#!/usr/bin/env python3

import pandas as pd


def inverse_series(s):
    """
    Create a new Series by swapping the indices and values of the input Series.

    Parameters:
    s (pd.Series): The input Series.

    Returns:
    pd.Series: The new Series with swapped indices and values.
    """
    # Using the Series constructor with the original Series values as the index
    # and the original Series index as the data.
    return pd.Series(data=s.index, index=s.values)


def main():
    # Test the function
    d = {2001: "Bush", 2005: "Bush", 2009: "Obama", 2013: "Obama", 2017: "Trump"}
    s = pd.Series(d, name="Presidents")
    print("Original Series:")
    print(s)

    inversed = inverse_series(s)
    print("\nInversed Series:")
    print(inversed)

    # Demonstrate what happens with duplicate values
    print("\nAccessing 'Bush' in the Inversed Series:")
    print(inversed['Bush'])


if __name__ == "__main__":
    main()
