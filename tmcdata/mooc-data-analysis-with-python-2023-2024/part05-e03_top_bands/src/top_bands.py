#!/usr/bin/env python3

import pandas as pd


def top_bands():
    # Read the DataFrames from the files
    bands_df = pd.read_csv('src/bands.tsv', sep='\t')
    top40_df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')

    # Standardize the text in the join columns
    bands_df['Band'] = bands_df['Band'].str.upper().str.strip()
    top40_df['Artist'] = top40_df['Artist'].str.upper().str.strip()

    # Perform the merge
    merged_df = pd.merge(top40_df, bands_df, how='inner',
                         left_on='Artist', right_on='Band')
    return merged_df


def main():
    merged_df = top_bands()
    print(merged_df)


if __name__ == "__main__":
    main()
