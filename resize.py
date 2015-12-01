import PIL
from PIL import Image
from tkinter import Tk
import tkinter.filedialog as tkdialog
import os
import re


""" Pyhon programm to resize all images in a folder to the selected width and put them
    in the drawable-xxhdpi folder of AndroidUniversalPrototypes
"""
basewidth = 1000
xxhdpi_directory = r"/Users/Florian/AndroidStudioProjects/AndroidUniversalPrototypes/app/src/main/res/drawable-xxhdpi/"

# Ask for image directory
Tk().withdraw()
directory = tkdialog.askdirectory()

# Move to directory
os.chdir(directory)

# Apply only to images (very rudimentary filtering, needs improvement)
pattern = re.compile('(.*).(?:jpg|gif|png)')  # TODO Improve regex

for file in os.listdir(directory):
    if pattern.match(file):
        img = Image.open(file)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

        os.remove(file)

        # Delete the file if existing, rewrite the updated version
        img.save(''.join([xxhdpi_directory, file]))


# img = Image.open('')