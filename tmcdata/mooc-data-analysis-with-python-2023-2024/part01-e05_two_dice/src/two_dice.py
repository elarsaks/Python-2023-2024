#!/usr/bin/env python3

def main():
    # Create a list of tuples where the sum of the dice rolls is 5
    combinations = [(dice1, dice2) for dice1 in range(1, 7)
                    for dice2 in range(1, 7) if dice1 + dice2 == 5]

    # Print each combination
    for combination in combinations:
        print(combination)


if __name__ == "__main__":
    main()
