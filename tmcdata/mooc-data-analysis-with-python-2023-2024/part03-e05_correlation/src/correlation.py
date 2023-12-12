#!/usr/bin/env python3

import scipy.stats
import numpy as np


def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values


def lengths():
    data = load()
    # Extracting sepal length and petal length
    sepal_length = data[:, 0]
    petal_length = data[:, 2]

    # Compute Pearson correlation
    correlation, _ = scipy.stats.pearsonr(sepal_length, petal_length)
    return correlation


def correlations():
    data = load()
    # Compute the correlation matrix
    corr_matrix = np.corrcoef(data.T)  # Transpose to get variables as columns
    return corr_matrix


def main():
    print("Pearson correlation between sepal length and petal length:", lengths())
    print("Correlation matrix of all variables:\n", correlations())


if __name__ == "__main__":
    main()
