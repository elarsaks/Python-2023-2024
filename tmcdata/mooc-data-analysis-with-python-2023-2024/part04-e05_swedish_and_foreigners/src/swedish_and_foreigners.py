#!/usr/bin/env python3

import pandas as pd


def swedish_and_foreigners():

    # Read the dataset
    df = pd.read_csv('src/municipal.tsv', sep='\t', index_col=0)

    # Get only the municipalities
    municipalities = df.loc['Akaa':'Äänekoski']

    # Filter rows where both Swedish-speaking and foreigners are above 5%
    filtered = municipalities[(municipalities['Share of Swedish-speakers of the population, %'] > 5) &
                              (municipalities['Share of foreign citizens of the population, %'] > 5)]

    # Select only the required columns
    result = filtered[['Population', 'Share of Swedish-speakers of the population, %',
                       'Share of foreign citizens of the population, %']]

    return result


def main():
    print(swedish_and_foreigners())
    return


if __name__ == "__main__":
    main()
