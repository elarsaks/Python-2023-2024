import pandas as pd
from sklearn.linear_model import LinearRegression


def mystery_data():
    # Read the data
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')

    # Split the data into features and response
    X = df.iloc[:, :-1]  # All rows, all columns except the last one
    y = df.iloc[:, -1]   # All rows, only the last column

    # Create and fit the model
    model = LinearRegression(fit_intercept=False)
    model.fit(X, y)

    # Return the coefficients
    return model.coef_


def main():
    # Get the coefficients
    coefficients = mystery_data()

    # Print the coefficients
    for i, coef in enumerate(coefficients, start=1):
        print(f"Coefficient of X{i} is {coef}")

    # Discuss which features might be important
    print("\nWhich features you think are needed to explain the response Y?")
    # Add your discussion or analysis here


if __name__ == "__main__":
    main()
