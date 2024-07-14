from PIL import Image, ImageSequence
import os

def gif_to_images(file):
    # Open the GIF file
    with Image.open(file) as img:
        pathname = file[:-4]
        if not os.path.exists(os.path.join(os.getcwd(), pathname)):
            os.makedirs(pathname)
        else:
            remove_pngs(file[:-4] + "/")
        # Iterate through each frame in the GIF
        frame_number = 0
        for frame in ImageSequence.Iterator(img):
            # Assuming RGBA for transparency handling
            # You can convert "RGBA" to "RGB" if you don't need transparency
            frame = frame.convert("RGB")
            
            frame.save(os.path.join(pathname, f"frame_{frame_number}.png"), "PNG")
            frame_number += 1
def remove_pngs(directory):
    files = os.listdir(directory)
    for file in files:
        if file[-4:] == ".png":
            os.remove(os.path.join(directory, file))

def png_to_tuples(file):
    image = Image.open(file)
    image = image.convert("RGB")
    width, height = image.size
    colours = []
    for y in range(height):
        colours.append([])
        for x in range(width):
            colours[len(colours) - 1].append(image.getpixel((x, y)))
    return colours

gif_to_images(os.getcwd() + "/laser-strong.gif")
print(png_to_tuples(os.getcwd() + "/laser-strong/frame_0.png"))