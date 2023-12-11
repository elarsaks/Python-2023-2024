import numpy as np


def column_comparison(a):
    # Boolean indexing to filter rows where the second column value is greater than the second-to-last column value
    return a[a[:, 1] > a[:, -2]]


def main():
    # Example array
    arr = np.array([[8, 9, 3, 8, 8],
                    [0, 5, 3, 9, 9],
                    [5, 7, 6, 0, 4],
                    [7, 8, 1, 6, 2],
                    [2, 1, 3, 5, 8]])

    # Testing the function
    result = column_comparison(arr)
    print(result)


if __name__ == "__main__":
    main()
