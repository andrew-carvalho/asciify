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

    image_array = transform_image_to_2d_array(image)
    print("Successfully constructed pixel matrix!")
    print("Pixel matrix size: " + str(len(image_array[0])) + " x " + str(len(image_array)))

def transform_image_to_2d_array(image):
    image_data = image.getdata()

    image_array = []

    for y in range(0, image.height):
        image_array.append([])
        for x in range(0, image.width):
            image_array[y].append(image_data.getpixel((x,y)))

    return image_array


if __name__ == "__main__":
    main()