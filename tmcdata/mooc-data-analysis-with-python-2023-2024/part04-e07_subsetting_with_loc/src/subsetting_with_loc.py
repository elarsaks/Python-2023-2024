#!/usr/bin/env python3

import pandas as pd


def subsetting_with_loc():
    file_path = 'src/municipal.tsv'
    df = pd.read_csv(file_path, sep='\t', index_col=0)

    # Using loc to select rows from 'Akaa' to 'Äänekoski' and the specified columns
    result = df.loc['Akaa':'Äänekoski', [
        'Population', 'Share of Swedish-speakers of the population, %', 'Share of foreign citizens of the population, %']]
    return result


def main():
    print(subsetting_with_loc())
    return


if __name__ == "__main__":
    main()
