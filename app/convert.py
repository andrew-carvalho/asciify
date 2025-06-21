from constants import CHAR_MAP, RGB_RANGE, CHAR_SCALE


def transform_image_to_ascii_2d_array(image):
    image_data = image.getdata()

    image_array = []

    for y in range(0, image.height):
        image_array.append([])
        for x in range(0, image.width):
            brightness_value = get_brightness_value_from_pixel(
                image_data.getpixel((x, y))
            )
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
