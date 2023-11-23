#!/usr/bin/env python3

def sum_equation(L):
    if not L:  # Check if the list is empty
        return "0 = 0"
    else:
        # Join numbers with " + ", calculate sum, and format the string
        equation = " + ".join(map(str, L))
        total = sum(L)
        return f"{equation} = {total}"


def main():
    pass


if __name__ == "__main__":
    main()
