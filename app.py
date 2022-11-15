"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://www.gradescope.com/courses/460101)
    - Lesson Plan: https://tech-at-du.github.io/ACS-3230-Web-Security/#/Lessons/Steganography

BIGGEST HINT: The secret image is hidden in the binary of the pixels in the red channel of the image.
That is, the value of the binary of each red pixel is 1 if the hidden image was 1 at that location,
and 0 if the hidden image was also 0. Hidden image is a piece of text, black and white piece of text.

Your task is to iterate though each pixel in the encoded image and set the decode_image pixel
to be (0, 0, 0) black or (255, 255, 255) white depending on the value of that binary.

Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed - DONE
    3. Your own image encoded with hidden secret text!
"""
# TODO: Run `pip3 install Pillow` before running the code.
from PIL import Image


def decode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]
    # red_channel = encoded_image.getchannel(0)

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # TODO: Using the variables declared above, replace `print(red_channel)` with a complete implementation:

    # loop through x_size, and y_size
    for x in range(x_size):
      for y in range(y_size):
        # at each, pixels[x, y] position, get the red_channel.getpixel((x, y))
        red_value = red_channel.getpixel((x, y))
        # convert it to binary
        binary = bin(red_value)
        # Get the LSB (rightmost value of binary string)
        lsb = int(binary[len(binary) - 1])
        print(lsb)

        # Use LSB to decide to set the new pixel to be either (0, 0, 0) black or (255, 255, 255) white
        if lsb == 1:
          pixels[x, y] = (255, 255, 255)
          # decoded_image.putpixel((x, y), (255, 255, 255))
        elif lsb == 0:
          pixels[x, y] = (0, 0, 0)
          # decoded_image.putpixel((x, y), (0, 0, 0))

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    pass


def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass


# decode_image('dog.png')
decode_image('encoded_sample.png')
