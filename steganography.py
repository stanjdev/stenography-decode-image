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
from PIL import Image, ImageDraw, ImageFont


def decode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    Takes in a string to a png image and decodes the image to reveal hidden message
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
        # print(lsb)

        # Use LSB to decide to set the new pixel to be either (0, 0, 0) black or (255, 255, 255) white
        if lsb == 1:
          pixels[x, y] = (255, 255, 255)
          # decoded_image.putpixel((x, y), (255, 255, 255))
        elif lsb == 0:
          pixels[x, y] = (0, 0, 0)
          # decoded_image.putpixel((x, y), (0, 0, 0))

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png, secret_message = "default secret"):
    """
    TODO: Add docstring and complete implementation.
    """

    # ordinary image
    image = Image.open(path_to_png)

    # Isolate the red channel of the original image
    red_channel = image.split()[0]

    # Create a new PIL image with the same size as the original image:
    # write the original pixels and the encoded pixels
    encoded_image = Image.new("RGB", image.size)
    pixels = encoded_image.load()
    x_size, y_size = image.size

    # write_text helper method to create image with white text over black background.
    secret_message_canvas = write_text(secret_message, x_size, y_size)
    pixels_secret = secret_message_canvas.load()

    for x in range(x_size):
      for y in range(y_size):
        red_value = red_channel.getpixel((x, y))
        binary = bin(red_value)
        (r, g, b, a) = image.load()[x, y]
        # at the x,y see if pixel is white.
        if pixels_secret[x,y] == (255, 255, 255):
          # if so, alter the dog's binary string's lsb to be 1.
          updated_binary = binary[0:-1] + "1"
          decimal = int(updated_binary, 2)
          pixels[x, y] = (decimal, g, b, 255)
        elif pixels_secret[x,y] == (0, 0, 0):
          # flip it to be 0
          updated_binary = binary[0:-1] + "0"
          decimal = int(updated_binary, 2)
          pixels[x, y] = (decimal, g, b, 255)

    encoded_image.save("encoded_image.png")


def write_text(text_to_write, x_size = 200, y_size = 100):
    """
    TODO: Add docstring and complete implementation.
    This will take a string and convert it to a black and white image of the string
    """

    # Create black and white image same size as image, with text as white and black background.
    font = ImageFont.load_default()
    canvas = Image.new('RGB', (x_size, y_size), "black")

    draw = ImageDraw.Draw(canvas)
    draw.text((10, 10), text_to_write, "white", font)

    canvas.save("written_text_canvas.png")
    return canvas



# # DECODE THE PROVIDED SAMPLE IMAGE
decode_image('encoded_sample.png')


# # ENCODE AN IMAGE WITH A SECRET MESSAGE
# encode_image('dog.png', 'Focus Hocus Pocus')
# # AND THEN
# decode_image('encoded_image.png')


# # Encode Example 2:
# encode_image('purple-flowers.png', 'Lotus Flower Bomb Flower Power Away Into the skies')
decode_image('encoded_image.png')
