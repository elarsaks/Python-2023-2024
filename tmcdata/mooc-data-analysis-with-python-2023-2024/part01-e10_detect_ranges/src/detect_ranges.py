#!/usr/bin/env python3

def detect_ranges(L):
    # Sort the list
    sorted_lst = sorted(L)

    # Initialize the result list and a temporary start for the current range
    result = []
    range_start = None

    # Iterate through the sorted list
    for i in range(len(sorted_lst)):
        # If range_start is None, we are not currently tracking a range
        if range_start is None:
            range_start = sorted_lst[i]

        # Check if we are at the end of the list or the next number is not consecutive
        if i == len(sorted_lst) - 1 or sorted_lst[i] + 1 != sorted_lst[i + 1]:
            # If the current number is directly after range_start, it's not a range
            if sorted_lst[i] == range_start:
                result.append(sorted_lst[i])
            else:
                # Add the range (start, end exclusive) to the result
                result.append((range_start, sorted_lst[i] + 1))
            range_start = None

    return result


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
