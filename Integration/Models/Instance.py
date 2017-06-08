""" Instance module """
from Folder import Folder

class Instance:
    """ This class represents an Instace file (DICOM), that is inside a Series folder. """

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def read_property(self, coords):
        return "A property from coords: " + coords + " of path " + str(self.path_to_file)
