from PIL import Image

def main():
    image = None
    
    try:
        image = Image.open("example.jpg")
    except OSError:
        print("Error while loading image!")
        quit
    
    print("Successfully loaded image!")
    print("Image size: " + str(image.width) + " x " + str(image.height))

    image_bightness_array = transform_image_to_2d_brightness_array(image)
    print("Successfully constructed brightness matrix!")
    print("Brightness matrix size: " + str(len(image_bightness_array[0])) + " x " + str(len(image_bightness_array)))

def transform_image_to_2d_brightness_array(image):
    image_data = image.getdata()

    image_bightness_array = []

    for y in range(0, image.height):
        image_bightness_array.append([])
        for x in range(0, image.width):
            rgb_values = image_data.getpixel((x,y))
            brightness_value = sum(rgb_values) / len(rgb_values)
            image_bightness_array[y].append(brightness_value)

    return image_bightness_array

if __name__ == "__main__":
    main()