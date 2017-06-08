""" Instance module """
from Folder import Folder
import string
import random

class Instance:
    """ This class represents an Instace file (DICOM), that is inside a Series folder. """
    series_path = None

    def __init__(self):
        self.path_to_file = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

    def read_property(self, coords):
        return "A property from coords: " + coords + " of path " + str(self.path_to_file)
