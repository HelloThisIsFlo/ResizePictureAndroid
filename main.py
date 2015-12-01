from tkinter import Tk
import tkinter.filedialog as tkdialog
import os
from resize import Resize

""" Pyhon programm to resize all images in a folder to the selected width and put them
    in the drawable-xxhdpi folder of AndroidUniversalPrototypes

    Future evolutions :
    - Select only the base directory of the project or module and automatically add to the right folder, or prompt
     for module if more than one
    -
"""


def single_directory_version():
    basewidth = 288
    xxhdpi_directory =\
        r"/Users/Florian/AndroidStudioProjects/AndroidUniversalPrototypes/app/src/main/res/drawable-xxhdpi/"

    # Ask for image directory
    Tk().withdraw()
    directory = tkdialog.askdirectory()

    # Move to directory
    os.chdir(directory)

    tool = Resize()

    for file in os.listdir(directory):
        tool.resize_keep_aspect_ratio(file, basewidth)


def files_version():
    width_dp = 64  # equals to mdpi pixel size

    module_directory = r"/Users/Florian/AndroidStudioProjects/AndroidUniversalPrototypes/app/"

    # Ask for files directory
    Tk().withdraw()
    files = tkdialog.askopenfilenames(initialdir=module_directory)
    if len(files) == 0:
        return

    tool = Resize(module_directory)
    for file in files:
        tool.resize_file(file, width_dp)
        # os.remove(file)


if __name__ == '__main__':
    files_version()

