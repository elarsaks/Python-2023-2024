import matplotlib.pyplot as plt
import numpy as np


def subfigures(a):
    # Create a figure with two subplots (axes)
    fig, (ax1, ax2) = plt.subplots(1, 2)

    # Plot on the first subplot (ax1)
    ax1.plot(a[:, 0], a[:, 1])
    ax1.set_title('Line Plot')
    ax1.set_xlabel('X-axis')
    ax1.set_ylabel('Y-axis')

    # Scatter plot on the second subplot (ax2)
    scatter = ax2.scatter(a[:, 0], a[:, 1], c=a[:, 2], s=a[:, 3])
    ax2.set_title('Scatter Plot')
    ax2.set_xlabel('X-axis')
    ax2.set_ylabel('Y-axis')

    # Show the plot
    plt.show()


def main():
    # Test data
    # Columns: x, y, color, size
    data = np.array([
        [1, 2, 3, 100],
        [2, 3, 4, 200],
        [3, 4, 5, 300],
        [4, 5, 6, 400]
    ])

    subfigures(data)


if __name__ == "__main__":
    main()
