#!/usr/bin/env python3

import math


def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ").lower()

        if shape == "":
            break
        elif shape == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            area = 0.5 * base * height
            print(f"The area is {area:.6f}")
        elif shape == "rectangle":
            width = float(input("Give width of the rectangle: "))
            height = float(input("Give height of the rectangle: "))
            area = width * height
            print(f"The area is {area:.6f}")
        elif shape == "circle":
            radius = float(input("Give radius of the circle: "))
            area = math.pi * radius ** 2
            print(f"The area is {area:.6f}")
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
