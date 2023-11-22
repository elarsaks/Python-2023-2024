#!/usr/bin/env python3

def find_matching(L, pattern):
    matching_indices = []
    for index, string in enumerate(L):
        if pattern in string:
            matching_indices.append(index)
    return matching_indices


def main():
    pass


if __name__ == "__main__":
    main()
