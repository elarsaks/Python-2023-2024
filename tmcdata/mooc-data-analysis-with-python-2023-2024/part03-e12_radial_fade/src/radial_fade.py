import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def center(a):
    """
    Calculate the center of the image.
    :param a: numpy array representing the image.
    :return: Tuple (center_y, center_x) representing the center coordinates.
    """
    return (a.shape[0] / 2 - 0.5, a.shape[1] / 2 - 0.5)


def radial_distance(a):
    """
    Compute the Euclidean distance of each pixel from the center of the image.
    :param a: numpy array representing the image.
    :return: numpy array of the same height and width as a, with each element
             representing the distance of that pixel from the center.
    """
    h, w = a.shape[:2]
    center_y, center_x = center(a)
    y, x = np.ogrid[:h, :w]
    return np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)


def radial_mask(a):
    """
    Create a radial mask where values near the center are close to 1 and values
    near the edges are closer to 0.
    :param a: numpy array representing the image.
    :return: numpy array of the same height and width as a, with values between 0 and 1.
    """
    dist = radial_distance(a)
    max_dist = np.max(dist)
    mask = 1 - dist / max_dist
    # Ensure the center pixel's mask value is exactly 1
    cy, cx = center(a)
    mask[int(cy), int(cx)] = 1
    return mask


def radial_fade(a):
    """
    Apply a radial fade to the image.
    :param a: numpy array representing the image.
    :return: numpy array representing the faded image.
    """
    mask = radial_mask(a)[..., np.newaxis]
    return a * mask


def main():
    """
    Main function to load an image, apply radial fading, and display the results.
    """
    # Load the image
    img = np.array(Image.open('src/painting.png'))

    # Create the mask and faded image
    mask = radial_mask(img)
    faded_img = radial_fade(img)

    # Plotting
    fig, axes = plt.subplots(3, 1, figsize=(6, 18))

    axes[0].imshow(img)
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    axes[1].imshow(mask, cmap='gray')
    axes[1].set_title('Radial Mask')
    axes[1].axis('off')

    axes[2].imshow(faded_img.astype(np.uint8))
    axes[2].set_title('Faded Image')
    axes[2].axis('off')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
