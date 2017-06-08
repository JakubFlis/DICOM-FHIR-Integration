""" Series module. """
import random
from Folder import Folder

class Series(Folder):
    """ This class represents a Series folder, that is inside a Study folder. """
    path = None

    def __init__(self, instances, path):
        self.instances = instances
        self.path = path

    def get_any_dicom(self):
        return random.choice(self.instances)
        