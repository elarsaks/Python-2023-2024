#!/usr/bin/env python3

import pandas as pd


def main():
    file_path = 'src/municipal.tsv'

    # Load the dataset
    # Use sep='\t' for tab-separated values
    df = pd.read_csv(file_path, sep='\t')

    # Print the shape of the DataFrame
    print(f"Shape: {df.shape[0]},{df.shape[1]}")

    # Print the column names
    print("Columns:")
    for col in df.columns:
        print(col)


# Run the main function
if __name__ == "__main__":
    main()
