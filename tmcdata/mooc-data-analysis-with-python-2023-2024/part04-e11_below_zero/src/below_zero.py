#!/usr/bin/env python3

import pandas as pd


def below_zero():
    # Read the DataFrame from the specified file
    df = pd.read_csv('src/kumpula-weather-2017.csv')

    # Filter the DataFrame for days with temperatures below zero
    below_zero_df = df[df['Air temperature (degC)'] < 0]

    # Count the number of days
    num_days_below_zero = below_zero_df.shape[0]

    return num_days_below_zero


def main():
    days_below_zero = below_zero()
    print(f"Number of days below zero: {days_below_zero}")


if __name__ == "__main__":
    main()
