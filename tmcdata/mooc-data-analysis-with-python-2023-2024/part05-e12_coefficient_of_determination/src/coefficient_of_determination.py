#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression


def coefficient_of_determination():
    # Read the data
    df = pd.read_csv('src/mystery_data.tsv', sep='\t')

    # Split the data into features and response
    X = df.iloc[:, :-1]  # All rows, all columns except the last one
    y = df.iloc[:, -1]   # All rows, only the last column

    # Initialize the linear regression model
    model = LinearRegression()

    # Fit the model with all features and calculate R2-score
    model.fit(X, y)
    r2_scores = [model.score(X, y)]

    # Calculate R2-score for each feature
    for i in range(X.shape[1]):
        Xi = X.iloc[:, i].values.reshape(-1, 1)
        model.fit(Xi, y)
        r2_scores.append(model.score(Xi, y))

    return r2_scores


def main():
    r2_scores = coefficient_of_determination()

    # Print the R2-scores
    features = ['X', 'X1', 'X2', 'X3', 'X4', 'X5']
    for feature, score in zip(features, r2_scores):
        print(f"R2-score with feature(s) {feature}: {score}")

    # Experiment with fitting the intercept and without fitting the intercept
    # Add your experiment code here if needed


if __name__ == "__main__":
    main()
