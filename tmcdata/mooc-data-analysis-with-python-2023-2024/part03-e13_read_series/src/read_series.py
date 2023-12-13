#!/usr/bin/env python3
# This shebang line specifies the interpreter path. It ensures the script runs with the Python interpreter
# found in the user's PATH environment variable, which is typically the default Python 3 interpreter.

# Importing the pandas library, commonly referred to as 'pd'.
import pandas as pd


def read_series():
    # This function reads input from the user to create a pandas Series.
    series_data = {}  # Initialize an empty dictionary to store series data.

    while True:  # Start an infinite loop to continuously read user input.
        line = input("Enter index and value (or empty line to finish): ")
        # Prompt the user to enter the index and value, separated by a space.

        if line == "":
            break  # If the input line is empty, break out of the loop.

        # Split the input line into parts based on whitespace.
        parts = line.split()

        if len(parts) != 2:
            # If the input line does not split into exactly two parts, raise a ValueError.
            raise ValueError("Malformed input: '{}'".format(line))

        # Unpack the two parts into index and value variables.
        index, value = parts
        # Add the index and value to the series_data dictionary.
        series_data[index] = value

    # Convert the dictionary into a pandas Series and return it.
    return pd.Series(series_data)


def main():
    # Main function to execute the script.
    try:
        # Try to read a series using the read_series function.
        series = read_series()
        print("Series:")  # Print a header for the output.
        print(series)  # Print the created pandas Series.
    except ValueError as e:
        # If a ValueError is raised in the read_series function, catch it and print the error message.
        print(e)


if __name__ == "__main__":
    # This conditional statement checks if the script is being run as the main program and not being imported as a module.
    main()  # Call the main function.
