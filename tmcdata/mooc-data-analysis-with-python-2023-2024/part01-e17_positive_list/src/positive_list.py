#!/usr/bin/env python3

def positive_list(L):
    # Define a function that checks if a number is positive
    def is_positive(n):
        return n > 0

    # Use filter to apply the is_positive function to the list of numbers
    filtered_numbers = filter(is_positive, L)

    # Convert the filter object to a list and return it
    return list(filtered_numbers)


def main():
    pass


if __name__ == "__main__":
    main()
