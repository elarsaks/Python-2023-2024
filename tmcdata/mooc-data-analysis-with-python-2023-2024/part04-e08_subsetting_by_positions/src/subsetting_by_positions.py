#!/usr/bin/env python3

import pandas as pd


def subsetting_by_positions():
    # Read the TSV dataset, specifying the delimiter as '\t'
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', delimiter='\t')

    # Subset the DataFrame using iloc to get the top 10 entries and the columns for Title and Artist
    # Adjust the column indices to match the positions of 'Title' and 'Artist'
    # 'Title' is at index 2 and 'Artist' is at index 3
    result_df = df.iloc[0:10, [2, 3]]

    return result_df


def main():
    result = subsetting_by_positions()
    print(result)


if __name__ == "__main__":
    main()
