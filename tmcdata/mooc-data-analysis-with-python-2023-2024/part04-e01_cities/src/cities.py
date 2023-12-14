#!/usr/bin/env python3

import pandas as pd


def cities():
    # Define the data
    data = {
        'Population': [643272, 279044, 231853, 223027, 201810],
        'Total area': [715.48, 528.03, 689.59, 240.35, 3817.52]
    }

    # Define the index (city names)
    index = ['Helsinki', 'Espoo', 'Tampere', 'Vantaa', 'Oulu']

    # Create the DataFrame
    df = pd.DataFrame(data, index=index)

    return df


def main():
    print(cities())
    return


if __name__ == "__main__":
    main()
