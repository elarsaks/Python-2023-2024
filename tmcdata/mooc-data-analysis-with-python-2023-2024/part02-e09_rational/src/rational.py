#!/usr/bin/env python3

from math import gcd


class Rational(object):
    def __init__(self, numerator, denominator):
        # Constructor for the Rational class. It takes two arguments:
        # numerator and denominator for the rational number.
        if denominator == 0:
            # Denominator cannot be zero.
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()  # Simplify the rational number upon initialization.

    def _simplify(self):
        """ Simplify the rational number to its lowest terms. """
        common_divisor = gcd(self.numerator, self.denominator)
        # Divide the numerator by the greatest common divisor.
        self.numerator //= common_divisor
        # Divide the denominator by the greatest common divisor.
        self.denominator //= common_divisor

    def __add__(self, other):
        # Addition operation. Adds two rational numbers.
        new_numerator = self.numerator * other.denominator + \
            other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __sub__(self, other):
        # Subtraction operation. Subtracts one rational number from another.
        new_numerator = self.numerator * other.denominator - \
            other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __mul__(self, other):
        # Multiplication operation. Multiplies two rational numbers.
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __truediv__(self, other):
        # Division operation. Divides one rational number by another.
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Rational(new_numerator, new_denominator)

    def __eq__(self, other):
        # Equality operation. Checks if two rational numbers are equal.
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):
        # Less-than operation. Checks if one rational number is less than another.
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        # Greater-than operation. Checks if one rational number is greater than another.
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __str__(self):
        # String representation of the rational number.
        return f"{self.numerator}/{self.denominator}"


def main():
    # Demonstration of the Rational class functionality
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)  # Print the rational number r1
    print(r2)  # Print the rational number r2
    print(r1 * r2)  # Print the product of r1 and r2
    print(r1 / r2)  # Print the quotient of r1 and r2
    print(r1 + r2)  # Print the sum of r1 and r2
    print(r1 - r2)  # Print the difference of r1 and r2
    # Check if two rational numbers are equal
    print(Rational(1, 2) == Rational(2, 4))
    # Check if one rational number is greater than another
    print(Rational(1, 2) > Rational(2, 4))
    # Check if one rational number is less than another
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()
