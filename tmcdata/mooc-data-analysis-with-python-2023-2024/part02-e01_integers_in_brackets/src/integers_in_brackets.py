#!/usr/bin/env python3
import re


def integers_in_brackets(s):
    # This regular expression looks for numbers enclosed in brackets
    # It handles optional whitespace inside the brackets as well
    pattern = r'\[\s*([+-]?\d+)\s*\]'
    # Find all matches in the string
    matches = re.findall(pattern, s)
    # Convert all matches to integers
    return [int(number) for number in matches]


def main():
    pass


if __name__ == "__main__":
    main()
