#!/usr/bin/env python3

import pandas as pd


def powers_of_series(s, k):
    # Create a DataFrame from the Series
    df = pd.DataFrame({i: s**i for i in range(1, k+1)})

    return df


def main():
    # Test the function
    s = pd.Series([1, 2, 3, 4], index=list("abcd"))
    print(powers_of_series(s, 3))

    return


if __name__ == "__main__":
    main()
