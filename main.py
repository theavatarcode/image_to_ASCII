
import PIL.Image as PIL

ASCII = ['@', '#', "/", "S", "%", "?", "*", "+", ";", ":", ",", ".", "$", "O", "|", "Y", "$"]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    resized_imgae = image.resize((new_width, new_height))
    return (resized_imgae)

def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII[pixel//25] for pixel in pixels])
    return(characters)



def main(new_width=120):
    path = input('input image Path : ')
    try:
        image = PIL.open(path)
    except:
        print('An error open path file.')

    new_image_data = pixels_to_ascii(grayify(resize_image(image)))
    pixel_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:i+new_width] for i in range(0, pixel_count, new_width))

    print(ascii_image)

    with open("output.txt", "w") as f:
        f.write(ascii_image)

main()