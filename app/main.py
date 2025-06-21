from PIL import Image
from argparse import ArgumentParser
from constants import MAX_WIDTH, MAX_HEIGHT
from convert import transform_image_to_ascii_2d_array


def main():
    args = define_arguments()

    image = validate_file(args.filename)
    if image is None:
        return

    image = image.resize((int(args.width), int(args.height)))
    image_array = transform_image_to_ascii_2d_array(image)
    print_ascii(image, image_array)


def define_arguments():
    parser = ArgumentParser(description="A simple program that converts image to ASCII")

    parser.add_argument("filename", help="The image path to process")
    parser.add_argument(
        "-wt", "--width", help="The width of the ASCII art output", default=MAX_WIDTH
    )
    parser.add_argument(
        "-ht", "--height", help="The height of the ASCII art output", default=MAX_HEIGHT
    )

    return parser.parse_args()


def validate_file(filename):
    try:
        with Image.open(filename) as img:
            img.verify()
    except (IOError, SyntaxError):
        print("Please select a valid image file!")
        return None

    try:
        image = Image.open(filename)
        return image
    except OSError:
        print("Error while loading image!")
        return None


def print_ascii(image, image_array):
    for y in range(0, image.height):
        for x in range(0, image.width):
            print(image_array[y][x], end="")
        print()


if __name__ == "__main__":
    main()
