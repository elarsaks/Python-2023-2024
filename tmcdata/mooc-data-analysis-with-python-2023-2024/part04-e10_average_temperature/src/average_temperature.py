#!/usr/bin/env python3

import pandas as pd


def average_temperature():
    # Read the DataFrame from the specified file
    df = pd.read_csv('src/kumpula-weather-2017.csv')

    # Filter the DataFrame for the month of July (7)
    july_df = df[df['m'] == 7]

    # Calculate the average temperature
    avg_temp = july_df['Air temperature (degC)'].mean()

    return avg_temp


def main():
    avg_temp_july = average_temperature()
    print(f"Average temperature in July: {avg_temp_july:.1f}")


if __name__ == "__main__":
    main()
