#!/usr/bin/env python3

import pandas as pd

import pandas as pd


def snow_depth():
    # Read the DataFrame from the specified file
    df = pd.read_csv('src/kumpula-weather-2017.csv')

    # Filter the DataFrame for the year 2017
    df_2017 = df[df['Year'] == 2017]

    # Find the maximum snow depth
    max_snow = df_2017['Snow depth (cm)'].max()

    return max_snow


def main():
    max_snow_depth = snow_depth()
    print(f"Max snow depth: {max_snow_depth:.1f}")


if __name__ == "__main__":
    main()
