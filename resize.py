import PIL
from PIL import Image
import re
import os


class Resize:
    def __init__(self, module_directory):
        """
        :param module_directory: Must follow the pattern "PATH_TO_PROJECT/MODULE/"
        """
        self.base_directory = ''.join([module_directory, r"src/main/res/drawable-"])

        self.resolutions = {
            'xxhdpi/': 3,
            'xhdpi/': 2,
            'hdpi/': 1.5,
            'mdpi/': 1,
            'ldpi/': 0.75,
        }

        # Apply only to images (very rudimentary filtering, needs improvement)
        self.pattern = re.compile('(.*).(?:jpg|gif|png)')  # TODO Improve regex

    def resize_file(self, filepath, width_dp):

        # For every resolution resize with the correct factor and save in the corresponding directory
        for resolution_directory, factor in self.resolutions.items():
            img = self.__internal_resize(filepath, int(width_dp * factor))
            filename = os.path.basename(filepath)

            # Delete the file if existing, rewrite the updated version
            savelocation = ''.join([self.base_directory, resolution_directory, filename])
            # os.remove(savelocation)
            img.save(savelocation)

    def __internal_resize(self, filepath, width):
        if self.pattern.match(filepath):  # todo implement with decorator
            img = Image.open(filepath)
            wpercent = (width / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((width, hsize), PIL.Image.ANTIALIAS)
            return img
            # os.remove(filepath)

            # Delete the file if existing, rewrite the updated version
            # img.save(''.join([xxhdpi_directory, filepath]))
            print(filepath)
            print(os.path.basename(filepath))
