#!/usr/bin/env python3

import pandas as pd
import numpy as np


def special_missing_values():
    filename = 'src/UK-top40-1964-1-2.tsv'

    try:
        data = pd.read_csv(filename, sep='\t')

        # Ensure the required columns are present
        required_columns = ["Pos", "LW", "Title",
                            "Artist", "Publisher", "Peak Pos", "WoC"]
        if not all(col in data.columns for col in required_columns):
            raise ValueError(
                "The dataset does not contain the required columns.")

        # Replace 'New' and 'Re' with NaN
        data['LW'].replace({'New': np.nan, 'Re': np.nan}, inplace=True)

        # Convert 'LW' column to numeric
        data['LW'] = pd.to_numeric(data['LW'], errors='coerce')

        # Find rows where the position has dropped
        dropped_positions = data[data['LW'] < data['Pos']]

        return dropped_positions

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    print(special_missing_values())
    return


if __name__ == "__main__":
    main()
