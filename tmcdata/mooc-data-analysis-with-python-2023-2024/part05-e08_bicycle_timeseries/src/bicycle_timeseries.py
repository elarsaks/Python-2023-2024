import pandas as pd


def bicycle_timeseries():
    # Read the data
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')

    # Drop columns that are entirely NaN
    df = df.dropna(axis=1, how='all')

    # Check the format of the dates in 'Päivämäärä'
    print("Sample dates:", df['Päivämäärä'].head())

    # Convert 'Päivämäärä' to datetime and handle errors
    df['Päivämäärä'] = pd.to_datetime(
        df['Päivämäärä'], dayfirst=True, errors='coerce')

    # Check how many rows have NaT in 'Päivämäärä'
    nat_count = df['Päivämäärä'].isna().sum()
    print("Number of NaT values:", nat_count)

    # Drop rows where 'Päivämäärä' is NaT (not a time)
    df = df.dropna(subset=['Päivämäärä'])

    # Set 'Päivämäärä' as the index
    df.set_index('Päivämäärä', inplace=True)

    return df


def main():
    df = bicycle_timeseries()
    print(df.head())
    return None


if __name__ == "__main__":
    main()
