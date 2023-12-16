#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt


def cyclists_per_day():
    filepath = 'src/Helsingin_pyorailijamaarat.csv'

    # Read the data
    df = pd.read_csv(filepath, sep=';')

    # Finnish month names mapping
    finnish_months = {
        'tammi': 1, 'helmi': 2, 'maalis': 3, 'huhti': 4, 'touko': 5, 'kesä': 6,
        'heinä': 7, 'elo': 8, 'syys': 9, 'loka': 10, 'marras': 11, 'joulu': 12
    }

    # Parse the 'Päivämäärä' column to datetime
    df['Päivämäärä'] = df['Päivämäärä'].str.replace(
        r'(\D+)\s(\d+)\s(\D+)\s(\d+)', lambda m: f"{m.group(2)}-{finnish_months[m.group(3).lower()]}-{m.group(4)}", regex=True)
    df['Päivämäärä'] = pd.to_datetime(
        df['Päivämäärä'], format='%d-%m-%Y', errors='coerce')

    # Drop rows where 'Päivämäärä' is NaN
    df = df.dropna(subset=['Päivämäärä'])

    # Split 'Päivämäärä' into Year, Month, Day and convert to integers
    df['Year'] = df['Päivämäärä'].dt.year.astype(int)
    df['Month'] = df['Päivämäärä'].dt.month.astype(int)
    df['Day'] = df['Päivämäärä'].dt.day.astype(int)

    # Drop the original date column and any other unnecessary columns
    df = df.drop(['Päivämäärä'], axis=1, errors='ignore')

    # Group by Year, Month, Day and sum the counts
    daily_counts = df.groupby(['Year', 'Month', 'Day']).sum()

    return daily_counts


def main():

    daily_data = cyclists_per_day()

 # Diagnostic print statements
    print("DataFrame after processing:")
    print(daily_data.head())
    print("\nYears in the index:")
    print(daily_data.index.get_level_values(0).unique())

    # Check if 2017 is in the index
    if 2017 in daily_data.index.get_level_values(0):
        august_2017 = daily_data.loc[(2017, 8)]

        # Plotting
        august_2017.plot()
        plt.xlabel('Day')
        plt.ylabel('Number of Cyclists')
        plt.title('Daily Cyclists Count for August 2017')
        plt.xticks(range(1, 32))  # Setting x-axis ticks from 1 to 31
        plt.legend(loc='upper right')
        plt.grid(True)
        plt.show()
    else:
        print("No data available for the year 2017")


if __name__ == "__main__":
    main()
