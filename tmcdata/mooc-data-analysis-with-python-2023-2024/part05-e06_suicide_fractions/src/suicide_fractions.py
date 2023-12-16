import pandas as pd


def suicide_fractions(filepath):
    # Load the data
    df = pd.read_csv(filepath)

    # Calculate the fraction of suicides for each row
    df['suicide_fraction'] = df['suicides_no'] / df['population']

    # Group by country and calculate the mean suicide fraction
    country_means = df.groupby('country')['suicide_fraction'].mean()

    return country_means


# Example usage
filepath = 'src/suicide_data.csv'  # Replace with your actual file path
result = suicide_fractions(filepath)
print(result)
