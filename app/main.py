from PIL import Image
from argparse import ArgumentParser
from constants import MAX_WIDTH, MAX_HEIGHT
from convert import get_brightness_value_from_pixel, get_char_from_brightness_value, transform_image_to_ascii_2d_array

def main():
    parser = ArgumentParser(description="A simple program that convert image to ASCII")

    parser.add_argument("filename", help="The image path to process")
    parser.add_argument("-wt", "--width", help="The width of the ASCII art output", default=MAX_WIDTH)
    parser.add_argument("-ht", "--height", help="The height of the ASCII art output", default=MAX_HEIGHT)

    args = parser.parse_args()

    filename = args.filename

    if filename is None:
        print("Please inform the image path.")
        return
    
    image = None
    try:
        image = Image.open(filename)
    except OSError:
        print("Error while loading image!")
        return

    image = image.resize((int(args.width), int(args.height)))
    image_array = transform_image_to_ascii_2d_array(image)
    print_ascii(image, image_array)

def print_ascii(image, image_array):
    for y in range(0, image.height):
        for x in range(0, image.width):
            print(image_array[y][x], end="")
        print()

if __name__ == "__main__":
    main()
