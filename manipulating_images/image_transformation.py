import os
from PIL import Image

PATH = "path_to_save" # to save
SRC = "path_to_get_images"
count = 0

for file in os.listdir(SRC): # getting all the images in thr SRC directory
    try:
        im = Image.open(SRC + file) # this gets the absolute path to image file 
        im = im.resize((128,128)).rotate(-90) # resizing and rotating Image
        out = im.convert("RGB")
        out.save(PATH+file, "JPEG", quality=90) # converting to JPEG and saving
        count += 1
    except:
        print("inside except", file)
print("Number of files converted = ", count)
