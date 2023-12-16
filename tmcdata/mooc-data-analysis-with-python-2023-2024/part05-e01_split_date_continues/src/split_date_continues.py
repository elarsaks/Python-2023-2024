import pandas as pd
import numpy as np


def split_date_continues():
    # Read the data set
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')

    # Drop columns and rows that contain only missing values
    df.dropna(axis=1, how='all', inplace=True)
    df.dropna(axis=0, how='all', inplace=True)

    # Split the 'Päivämäärä' column
    split_data = df['Päivämäärä'].str.split(expand=True)
    split_data.columns = ['Weekday', 'Day', 'Month', 'Year', 'Time']

    # Convert Weekdays and Months
    weekday_map = {'ma': 'Mon', 'ti': 'Tue', 'ke': 'Wed',
                   'to': 'Thu', 'pe': 'Fri', 'la': 'Sat', 'su': 'Sun'}
    month_map = {'tammi': 1, 'helmi': 2, 'maalis': 3, 'huhti': 4, 'touko': 5,
                 'kesä': 6, 'heinä': 7, 'elo': 8, 'syys': 9, 'loka': 10, 'marras': 11, 'joulu': 12}

    split_data['Weekday'] = split_data['Weekday'].map(weekday_map)
    split_data['Month'] = split_data['Month'].map(month_map)

    # Convert 'Day', 'Month', 'Year', and 'Hour' to integers
    for col in ['Day', 'Month', 'Year']:
        split_data[col] = pd.to_numeric(
            split_data[col], errors='coerce').fillna(0).astype(int)

    split_data['Hour'] = split_data['Time'].str.split(':', expand=True)[0]
    split_data['Hour'] = pd.to_numeric(
        split_data['Hour'], errors='coerce').fillna(0).astype(int)

    # Drop the 'Time' and 'Päivämäärä' columns
    split_data.drop('Time', axis=1, inplace=True)
    df.drop('Päivämäärä', axis=1, inplace=True)

    # Concatenate the split date columns with the rest of the data
    result = pd.concat([split_data, df], axis=1)

    return result


def main():
    print(split_date_continues())


if __name__ == "__main__":
    main()
