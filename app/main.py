from PIL import Image
from argparse import ArgumentParser
from constants import CHAR_MAP, RGB_RANGE, MAX_WIDTH, MAX_HEIGHT, CHAR_SCALE

def main():
    parser = ArgumentParser(description="A simple program that convert image to ASCII")

    parser.add_argument("filename", help="The image path to process")
    parser.add_argument("width", help="The width of the ASCII art output")
    parser.add_argument("height", help="The height of the ASCII art output")

    args = parser.parse_args()

    image = None
    
    try:
        image = Image.open("example.jpg")
    except OSError:
        print("Error while loading image!")
        return

    image = image.resize((MAX_WIDTH, MAX_HEIGHT))
    image_array = transform_image_to_ascii_2d_array(image)
    print_ascii(image, image_array)

def transform_image_to_ascii_2d_array(image):
    image_data = image.getdata()

    image_array = []

    for y in range(0, image.height):
        image_array.append([])
        for x in range(0, image.width):
            brightness_value = get_brightness_value_from_pixel(image_data.getpixel((x,y)))
            char = get_char_from_brightness_value(brightness_value)
            image_array[y].append(char * CHAR_SCALE)

    return image_array

# Average method -> average the R, G and B values - (R + G + B) / 3
def get_brightness_value_from_pixel(rgb_values):
    return sum(rgb_values) / len(rgb_values)

def get_char_from_brightness_value(brightness_value):
    map_length = len(CHAR_MAP)
    scale = RGB_RANGE / map_length
    index = int(brightness_value / scale) % map_length
    return CHAR_MAP[index]

def print_ascii(image, image_array):
    for y in range(0, image.height):
        for x in range(0, image.width):
            print(image_array[y][x], end="")
        print()

if __name__ == "__main__":
    main()
