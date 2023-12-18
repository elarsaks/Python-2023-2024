import pandas as pd


def suicide_fractions():
    df = pd.read_csv('src/who_suicide_statistics.csv')
    df['suicide_fraction'] = df['suicides_no'] / df['population']
    country_means = df.groupby('country')['suicide_fraction'].mean()
    return country_means


def suicide_weather():
    # Load suicide fractions
    suicide_df = suicide_fractions()

    # Load temperature data
    temp_dfs = pd.read_html(
        'src/List_of_countries_by_average_yearly_temperature.html', index_col=0, header=0)
    temperature_df = temp_dfs[0]

    # Clean temperature data
    temperature_df['Average yearly temperature (1961–1990, degrees Celsius)'] = temperature_df['Average yearly temperature (1961–1990, degrees Celsius)'].replace(
        "\u2212", "-", regex=True).astype(float)

    # Align the two datasets
    common_df = suicide_df.to_frame().join(temperature_df, how='inner')

    # Calculate Spearman correlation
    spearman_corr = common_df['suicide_fraction'].corr(
        common_df['Average yearly temperature (1961–1990, degrees Celsius)'], method='spearman')

    return (len(suicide_df), len(temperature_df), len(common_df), spearman_corr)


def main():
    suicide_rows, temperature_rows, common_rows, spearman_correlation = suicide_weather()
    print(f"Suicide DataFrame has {suicide_rows} rows")
    print(f"Temperature DataFrame has {temperature_rows} rows")
    print(f"Common DataFrame has {common_rows} rows")
    print(f"Spearman correlation: {spearman_correlation:.2f}")


if __name__ == "__main__":
    main()
