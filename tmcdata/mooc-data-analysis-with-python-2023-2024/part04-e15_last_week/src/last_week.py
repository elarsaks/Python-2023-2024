#!/usr/bin/env python3

import pandas as pd
import numpy as np


def last_week():
    filename = 'src/UK-top40-1964-1-2.tsv'

    try:
        data = pd.read_csv(filename, sep='\t')

        # Create a DataFrame for last week's data
        last_week_data = data.copy()

        # Set all 'LW' values to nan as per the test requirement
        last_week_data['LW'] = np.nan

        # Handle missing data for dropped songs
        # Assuming that songs with 'WoC' (Weeks on Chart) == 1 are new and were not on the chart last week
        for col in ['Title', 'Artist', 'Publisher', 'Peak Pos', 'WoC']:
            last_week_data.loc[last_week_data['WoC'] == 1, col] = np.nan

        # Identify the maximum position from last week
        max_position = data['Pos'].max()

        # Add rows for missing positions (songs that dropped off the chart)
        missing_positions = pd.DataFrame({
            'Pos': range(max_position + 1, 41),
            'LW': [np.nan] * (40 - max_position),
            'Title': [np.nan] * (40 - max_position),
            'Artist': [np.nan] * (40 - max_position),
            'Publisher': [np.nan] * (40 - max_position),
            'Peak Pos': [np.nan] * (40 - max_position),
            'WoC': [np.nan] * (40 - max_position)
        })

        # Combine the data with missing positions
        last_week_data = pd.concat(
            [last_week_data, missing_positions], ignore_index=True)

        # Sort by 'Pos' to maintain the top 40 order
        last_week_data.sort_values(by='Pos', inplace=True)

        # Reset index
        last_week_data.reset_index(drop=True, inplace=True)

        return last_week_data

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()


def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
