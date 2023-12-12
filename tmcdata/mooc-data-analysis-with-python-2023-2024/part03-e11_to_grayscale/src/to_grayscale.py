import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def to_grayscale(rgb_image):
    # Compute the weighted sum of the RGB channels.
    return np.dot(rgb_image[..., :3], [0.2126, 0.7152, 0.0722])


def to_red(rgb_image):
    red_image = rgb_image.copy()
    red_image[:, :, 1] = 0  # Zero out the green channel
    red_image[:, :, 2] = 0  # Zero out the blue channel
    return red_image


def to_green(rgb_image):
    green_image = rgb_image.copy()
    green_image[:, :, 0] = 0  # Zero out the red channel
    green_image[:, :, 2] = 0  # Zero out the blue channel
    return green_image


def to_blue(rgb_image):
    blue_image = rgb_image.copy()
    blue_image[:, :, 0] = 0  # Zero out the red channel
    blue_image[:, :, 1] = 0  # Zero out the green channel
    return blue_image


def main():
    # Load the image
    rgb_image = np.array(Image.open('src/painting.png'))

    # Convert to grayscale
    # gray_image = to_grayscale(rgb_image)

    # Convert to red, green, blue images
    red_image = to_red(rgb_image)
    green_image = to_green(rgb_image)
    blue_image = to_blue(rgb_image)

    # Display the images
    plt.figure()

    # Grayscale image
    # plt.subplot(2, 2, 1)
    # plt.imshow(gray_image, cmap='gray')
    # plt.title('Grayscale')
    # plt.axis('off')

    # Red image
    plt.subplot(2, 2, 2)
    plt.imshow(red_image)
    plt.title('Red channel')
    plt.axis('off')

    # Green image
    plt.subplot(2, 2, 3)
    plt.imshow(green_image)
    plt.title('Green channel')
    plt.axis('off')

    # Blue image
    plt.subplot(2, 2, 4)
    plt.imshow(blue_image)
    plt.title('Blue channel')
    plt.axis('off')

    plt.show()


if __name__ == "__main__":
    main()
