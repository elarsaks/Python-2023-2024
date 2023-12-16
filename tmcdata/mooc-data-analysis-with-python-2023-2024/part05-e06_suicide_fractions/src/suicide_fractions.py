import pandas as pd


def suicide_fractions():
    # Load the data
    df = pd.read_csv('src/who_suicide_statistics.csv')

    # Calculate the fraction of suicides for each row
    df['suicide_fraction'] = df['suicides_no'] / df['population']

    # Group by country and calculate the mean suicide fraction
    country_means = df.groupby('country')['suicide_fraction'].mean()

    return country_means


def main():
    # Example usage
    result = suicide_fractions()
    print(result)

    return


if __name__ == "__main__":
    main()
