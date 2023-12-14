#!/usr/bin/env python3

import pandas as pd


def municipalities_of_finland():
    file_path = 'src/municipal.tsv'

    # Load the dataset with the first column as the index
    df = pd.read_csv(file_path, sep='\t', index_col=0)

    # Get only the municipalities
    mun_df = df.loc['Akaa':'Äänekoski']

    # Print the shape of the DataFrame
    print(f"Shape: {mun_df.shape[0]},{mun_df.shape[1]}")

    # Print the column names
    print("Columns:")
    for col in mun_df.columns:
        print(col)

    return mun_df


def main():
    municipalities_of_finland()
    return


if __name__ == "__main__":
    main()
