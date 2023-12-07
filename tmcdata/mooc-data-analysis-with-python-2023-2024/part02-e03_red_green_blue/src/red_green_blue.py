#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    with open(filename, 'r') as file:
        # Skip the first line
        next(file)

        result = []
        for line in file:
            # Find all non-whitespace sequences in the line
            parts = re.findall(r'\S+', line.strip())

            # Reformat to have fields separated by a single tab character
            # The first three parts are RGB values, the rest is the color name
            formatted_line = '\t'.join(parts[:3]) + '\t' + ' '.join(parts[3:])
            result.append(formatted_line)

        return result


def main():
    pass


if __name__ == "__main__":
    main()
