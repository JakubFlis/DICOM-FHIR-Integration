""" Series module. """
import random
from Folder import Folder

class Series(Folder):
    """ This class represents a Series folder, that is inside a Study folder. """

    def __init__(self, instances, path):
        self.instances = instances
        self.path = path
        self.random_dicom = random.choice(self.instances)
