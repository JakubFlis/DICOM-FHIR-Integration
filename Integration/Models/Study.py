""" Study module """
import random
from Folder import Folder

class Study(Folder):
    """ This class represents a Study folder, that is inside a Patient folder. """

    def __init__(self, series, path):
        self.series = series
        self.path = path
        self.random_dicom = random.choice(self.series).random_dicom
