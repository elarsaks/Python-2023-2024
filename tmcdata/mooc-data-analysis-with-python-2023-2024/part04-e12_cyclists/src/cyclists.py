#!/usr/bin/env python3

import pandas as pd


def cyclists():
    # Load the dataset
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", delimiter=';')

    # Remove empty rows at the end of the dataset
    df.dropna(how='all', inplace=True)

    # Drop columns that contain only missing values
    df.dropna(axis=1, how='all', inplace=True)

    return df


def main():
    # Call the function and print the result
    cleaned_data = cyclists()
    print(cleaned_data)


if __name__ == "__main__":
    main()
