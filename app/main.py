import PIL.Image

def main():
    try:
        image = PIL.Image.open("example.jpg")
        print("Successfully loaded image!")
        print("Image size: " + str(image.width) + " x " + str(image.height))
    except OSError:
        print("Error while loading image!")

if __name__ == "__main__":
    main()