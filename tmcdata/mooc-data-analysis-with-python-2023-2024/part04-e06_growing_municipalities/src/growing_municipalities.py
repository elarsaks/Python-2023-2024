#!/usr/bin/env python3

import pandas as pd

import pandas as pd


def growing_municipalities(df):
    # Count the number of municipalities with increasing population
    growing_count = df[df['Population change from the previous year, %'] > 0].shape[0]

    # Calculate the proportion as a decimal
    proportion = (growing_count / df.shape[0])

    return proportion


def main():
    file_path = 'src/municipal.tsv'  # Replace with your actual file path
    df = pd.read_csv(file_path, sep='\t', index_col=0)

    # Get only the municipalities
    municipalities = df.loc['Akaa':'Äänekoski']

    # Test the function with the subset of municipalities
    proportion = growing_municipalities(municipalities)

    # Format the proportion as a percentage with one decimal place
    formatted_proportion = f"{proportion * 100:.1f}"

    print(f"Proportion of growing municipalities: {formatted_proportion}%")


# Run the main function
if __name__ == "__main__":
    main()
