#!/usr/bin/env python3
import sys
import math


def summary(filename):
    # Open the file for reading
    with open(filename, 'r') as file:
        numbers = []  # List to store valid numbers from the file

        # Iterate over each line in the file
        for line in file:
            try:
                # Try to convert the line to a float
                numbers.append(float(line))
            except ValueError:
                # If conversion fails, skip the line
                continue

        # If no valid numbers were found, return zeros
        if len(numbers) == 0:
            return (0, 0, 0)

        # Calculate the sum of the numbers
        total_sum = sum(numbers)

        # Calculate the average (mean) of the numbers
        average = total_sum / len(numbers)

        # Calculate the variance, which is the average of the squared differences
        # from the mean. This is a part of the standard deviation calculation.
        variance = sum((x - average) ** 2 for x in numbers) / \
            (len(numbers) - 1)

        # Standard deviation is the square root of the variance. It represents
        # a measure of the amount of variation or dispersion of a set of values.
        stddev = math.sqrt(variance)

        return (total_sum, average, stddev)


def main():
    # Iterate over each filename passed as a command line argument
    for filename in sys.argv[1:]:
        total_sum, average, stddev = summary(filename)
        # Print the results with six decimal precision
        print(
            f"File: {filename} Sum: {total_sum:.6f} Average: {average:.6f} Stddev: {stddev:.6f}")


if __name__ == "__main__":
    main()
