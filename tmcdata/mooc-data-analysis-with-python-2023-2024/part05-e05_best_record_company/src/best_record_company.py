#!/usr/bin/env python3

import pandas as pd


def best_record_company():
    # Load the data
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', delimiter='\t')

    # Group by record company and sum the weeks on chart
    company_woc = df.groupby('Publisher')['WoC'].sum()

    # Identify the best record company
    best_company = company_woc.idxmax()

    # Filter the DataFrame for the best record company
    best_company_singles = df[df['Publisher'] == best_company]

    return best_company_singles


def main():
    result = best_record_company()
    print(result)
    return


if __name__ == "__main__":
    main()
