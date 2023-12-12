#!/usr/bin/env python3

import numpy as np


def first_half_second_half(arr):
    # Check if the array has an even number of columns
    n, columns = arr.shape
    if columns % 2 != 0:
        raise ValueError("The number of columns should be even.")

    m = columns // 2

    # Calculate the sum of the first half and the second half of each row
    sum_first_half = np.sum(arr[:, :m], axis=1)
    sum_second_half = np.sum(arr[:, m:], axis=1)

    # Select rows where the sum of the first half is greater than the sum of the second half
    result = arr[sum_first_half > sum_second_half]

    return result


def main():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 9]])
    result = first_half_second_half(arr)
    print(result)


if __name__ == "__main__":
    main()
