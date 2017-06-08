""" Patient module. """
import random
from Folder import Folder

class Patient(Folder):
    """ This class represents a Patient folder, that is inside the root folder. """

    def __init__(self, studies, path):
        self.studies = studies
        self.path = path

    def get_any_dicom(self):
        return random.choice(self.studies)
        