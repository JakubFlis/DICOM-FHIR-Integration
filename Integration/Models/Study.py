""" Study module """
import random
from Folder import Folder
from Series import Series

class Study(Folder):
    """ This class represents a Study folder, that is inside a Patient folder. """
    path = None

    def __init__(self):
        self.series = [Series() for count in xrange(2)]

    def get_any_dicom(self):
        return random.choice(self.series).get_any_dicom()
