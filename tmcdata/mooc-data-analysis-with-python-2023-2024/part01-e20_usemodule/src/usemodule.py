#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle


def main():
    # Call the functions from here
    side1 = 3
    side2 = 4

    hyp = triangle.hypotenuse(side1, side2)
    print(
        f"The hypotenuse of a triangle with sides {side1} and {side2} is {hyp}")

    tri_area = triangle.area(side1, side2)
    print(
        f"The area of a right-angled triangle with sides {side1} and {side2} is {tri_area}")


if __name__ == "__main__":
    main()
