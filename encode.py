from PIL import Image
import os
from tkinter.filedialog import askopenfilename


def shorten_pixel_value(value):
    return str(hex(value).replace("0x", ""))


img_types = [("Image files", [".png", ".jpg"])]
img_filename = askopenfilename(initialdir=os.getcwd(), filetypes=img_types)

img = Image.open(img_filename, 'r')

if os.path.exists("image.iiif"):
    print("file exists, deleting...")
    os.remove("image.iiif")

print("creating file...")
newfile = open("image.iiif", "ab")

print("writing data...")
for y in range(img.height):
    row = b""
    for x in range(img.width):
        pixels = img.getpixel((x,y))
        row += b"," + bytes([pixels[0], pixels[1], pixels[2]])
    
    newfile.write(row)

print("done")
newfile.close()
