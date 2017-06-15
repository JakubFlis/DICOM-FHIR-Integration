""" Patient module. """
import random
from Folder import Folder

class Patient(Folder):
    """ This class represents a Patient folder, that is inside the root folder. """

    def __init__(self, studies, path):
        self.studies = studies
        self.path = path
        self.random_dicom = random.choice(self.studies).random_dicom
        