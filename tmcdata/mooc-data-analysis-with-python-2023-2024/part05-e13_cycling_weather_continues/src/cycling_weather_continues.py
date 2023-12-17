import pandas as pd
from sklearn.linear_model import LinearRegression


def cycling_weather_continues(station):
    # Read and preprocess weather data
    weather = pd.read_csv('src/kumpula-weather-2017.csv')
    weather = weather.dropna(subset=['Air temperature (degC)'])

    # Read cycling data
    cycling = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    cycling = cycling.dropna(how='all').dropna(axis=1, how='all')

    # Remove weekday abbreviations from the date strings
    cycling['Päivämäärä'] = cycling['Päivämäärä'].str.replace(
        r'^\D{2}\s', '', regex=True)

    # Convert 'Päivämäärä' to datetime
    cycling['Date'] = pd.to_datetime(
        cycling['Päivämäärä'], format='%d %b %Y %H:%M')

    # Merge datasets
    weather['Day'] = pd.to_datetime(weather['Year'].astype(
        str) + '-' + weather['m'].astype(str) + '-' + weather['d'].astype(str))
    data = pd.merge(cycling, weather, left_on='Day', right_on='Day')

    # Forward fill missing values
    data = data.fillna(method='ffill')

    # Linear regression
    X = data[[
        'Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    y = data[station]
    model = LinearRegression(fit_intercept=True)
    model.fit(X, y)
    coeffs = model.coef_
    score = model.score(X, y)

    return coeffs, score


def main():
    station = 'Baana'
    coeffs, score = cycling_weather_continues(station)
    print(f"Measuring station: {station}")
    print(
        f"Regression coefficient for variable 'precipitation': {coeffs[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coeffs[1]:.1f}")
    print(
        f"Regression coefficient for variable 'temperature': {coeffs[2]:.1f}")
    print(f"Score: {score:.2f}")


if __name__ == "__main__":
    main()
