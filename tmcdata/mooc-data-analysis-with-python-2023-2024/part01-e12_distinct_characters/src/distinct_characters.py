#!/usr/bin/env python3

def distinct_characters(L):
    result = {}
    for string in L:
        # Convert the string into a set to get distinct characters
        distinct_chars = set(string)
        # The number of distinct characters is the length of the set
        result[string] = len(distinct_chars)
    return result


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
