#!/usr/bin/env python3

def merge(L1, L2):
    # Initialize an empty list to store the merged list
    L = []

    # Initialize pointers for both lists
    i, j = 0, 0

    # Loop until we reach the end of one of the lists
    while i < len(L1) and j < len(L2):
        # Compare the elements at the current pointers of each list
        # and add the smaller one to the merged list
        if L1[i] < L2[j]:
            L.append(L1[i])
            i += 1
        else:
            L.append(L2[j])
            j += 1

    # Once we've reached the end of one of the lists,
    # add the remaining elements of the other list to the merged list
    while i < len(L1):
        L.append(L1[i])
        i += 1
    while j < len(L2):
        L.append(L2[j])
        j += 1

    return L


def main():
    pass


if __name__ == "__main__":
    main()
