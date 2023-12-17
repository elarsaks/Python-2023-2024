#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


def fit_line(x, y):
    # Reshape x to a 2D array for sklearn
    x_reshaped = x.reshape(-1, 1)

    # Create and fit the model
    model = LinearRegression().fit(x_reshaped, y)

    # Extract the slope and intercept
    slope = model.coef_[0]
    intercept = model.intercept_

    return slope, intercept


def main():
    # Example data
    x = np.array([0, 1, 2, 3, 4, 5])
    y = np.array([1, 3, 2, 5, 7, 8])

    # Fit the line
    slope, intercept = fit_line(x, y)

    # Print the results
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")

    # Plotting
    # Original data points
    plt.scatter(x, y, color='blue', label='Data points')
    plt.plot(x, slope * x + intercept, color='red',
             label='Fitted line')  # Fitted line

    # Labeling the plot
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear Fit with sklearn')
    plt.legend()

    # Show plot
    plt.show()


if __name__ == "__main__":
    main()
