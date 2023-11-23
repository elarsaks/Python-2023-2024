#!/usr/bin/env python3

def transform(s1, s2):
    # Split the strings into lists of words (numbers in string format)
    list1 = s1.split()
    list2 = s2.split()

    # Convert the string numbers to integers
    int_list1 = map(int, list1)
    int_list2 = map(int, list2)

    # Use zip to pair the numbers and multiply them
    result = [a * b for a, b in zip(int_list1, int_list2)]

    return result


def main():
    pass


if __name__ == "__main__":
    main()
