#!/usr/bin/env python3

import re


def file_listing(filename='src/listing.txt'):
    with open(filename, 'r') as file:
        content = file.readlines()

    # List to hold all the tuples
    result = []

    # Regular expression pattern to extract the required fields
    pattern = re.compile(r'\s*(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s+(\S+)')

    for line in content:
        match = pattern.search(line)
        if match:
            # Since we are sure there are exactly six groups based on our pattern, we can unpack them directly
            size, month, day, hour, minute, filename = match.groups()
            # Append a tuple to the result list
            result.append((int(size), month, int(day),
                          int(hour), int(minute), filename))

    return result


def main():
    pass


if __name__ == "__main__":
    main()
