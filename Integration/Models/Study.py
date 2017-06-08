""" Study module """
import random
from Folder import Folder

class Study(Folder):
    """ This class represents a Study folder, that is inside a Patient folder. """
    path = None

    def __init__(self, series, path):
        self.series = series
        self.path = path

    def get_any_dicom(self):
        return random.choice(self.series).get_any_dicom()
