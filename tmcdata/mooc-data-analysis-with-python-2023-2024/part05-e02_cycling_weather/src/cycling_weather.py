import pandas as pd


def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')

    # Ensure the dataset has the expected number of rows
    df = df.head(37128)

    # Split the 'Päivämäärä' column
    split_data = df['Päivämäärä'].str.split(expand=True)
    split_data.columns = ['Weekday', 'Day', 'Month', 'Year', 'Time']

    # Handle missing values or malformed data
    split_data.dropna(inplace=True)

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

    # Drop the 'Time' column
    split_data.drop('Time', axis=1, inplace=True)

    return split_data


def read_weather_data():
    # Read the weather data
    weather_df = pd.read_csv('src/kumpula-weather-2017.csv')

    # Rename columns for consistency
    weather_df.rename(
        columns={'Year': 'Year', 'm': 'Month', 'd': 'Day'}, inplace=True)

    return weather_df


def cycling_weather():
    # Process cycling data
    cycling_df = split_date()

    # Read and process weather data
    weather_df = read_weather_data()

    # Ensure column names are consistent for merging
    # Assuming 'Year', 'Month', and 'Day' are already consistent as per your provided code

    # Merge datasets on 'Year', 'Month', and 'Day'
    merged_df = pd.merge(cycling_df, weather_df, on=['Year', 'Month', 'Day'])

    # Drop unnecessary columns
    columns_to_drop = ['m', 'd', 'Time', 'Time zone']
    for col in columns_to_drop:
        if col in merged_df.columns:
            merged_df.drop(col, axis=1, inplace=True)

    return merged_df


def main():
    # Use the function to get the merged DataFrame
    result_df = cycling_weather()

    print(result_df)
    return


if __name__ == "__main__":
    main()
