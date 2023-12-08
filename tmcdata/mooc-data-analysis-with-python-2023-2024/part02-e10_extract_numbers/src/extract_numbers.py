#!/usr/bin/env python3

def extract_numbers(s):
    numbers = []
    for word in s.split():
        try:
            # Try converting to int first
            num = int(word)
        except ValueError:
            try:
                # If int conversion fails, try converting to float
                num = float(word)
            except ValueError:
                # If both conversions fail, continue to the next word
                continue
        numbers.append(num)
    return numbers


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))


if __name__ == "__main__":
    main()
