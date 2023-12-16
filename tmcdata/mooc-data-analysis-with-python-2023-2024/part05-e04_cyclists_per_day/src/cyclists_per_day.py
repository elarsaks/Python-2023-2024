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

    # Extract day, month name, and year from 'Päivämäärä'
    date_parts = df['Päivämäärä'].str.extract(r'\D+\s(\d+)\s(\D+)\s(\d+)')
    # Map Finnish month names to numbers
    date_parts[1] = date_parts[1].map(finnish_months)

    # Ensure all parts are numeric
    date_parts = date_parts.apply(pd.to_numeric, errors='coerce')

    # Create a new datetime column
    df['Date'] = pd.to_datetime(
        {'year': date_parts[2], 'month': date_parts[1], 'day': date_parts[0]}, errors='coerce')

    # Drop rows where 'Date' is NaT
    df = df.dropna(subset=['Date'])

    # Split 'Date' into Year, Month, Day
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day

    # Drop the original date column and any other unnecessary columns
    df = df.drop(['Päivämäärä', 'Date'], axis=1, errors='ignore')

    # Group by Year, Month, Day and sum the counts
    daily_counts = df.groupby(['Year', 'Month', 'Day']).sum()

    return daily_counts


def main():

    daily_data = cyclists_per_day()

 # Diagnostic print statements
    # print("DataFrame after processing:")
    # print(daily_data.head())
    # print("\nYears in the index:")
    # print(daily_data.index.get_level_values(0).unique())

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
