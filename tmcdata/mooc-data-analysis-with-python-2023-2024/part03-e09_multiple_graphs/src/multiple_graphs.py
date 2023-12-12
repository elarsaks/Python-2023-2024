#!/usr/bin/env python3

import matplotlib.pyplot as plt


def main():
    import matplotlib.pyplot as plt


def main():
    # First graph
    x1 = [2, 4, 6, 7]
    y1 = [4, 3, 5, 1]

    # Second graph
    x2 = [1, 2, 3, 4]
    y2 = [4, 2, 3, 1]

    # Plotting the first graph
    plt.plot(x1, y1, label='Graph 1')

    # Plotting the second graph
    plt.plot(x2, y2, label='Graph 2')

    # Adding title
    plt.title('Multiple Graphs in One Axes')

    # Adding labels
    plt.xlabel('X axis label')
    plt.ylabel('Y axis label')

    # Adding a legend
    plt.legend()

    # Display the plot
    plt.show()


if __name__ == "__main__":
    main()

    pass

if __name__ == "__main__":
    main()
