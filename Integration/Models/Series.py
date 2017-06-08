""" Series module. """
from Folder import Folder
from Instance import Instance
import random
import string

class Series(Folder):
    """ This class represents a Series folder, that is inside a Study folder. """
    path = None

    def __init__(self):
        self.instances = [Instance() for count in xrange(3)]
        self.path = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
        for instance in self.instances:
            instance.series_path = self.path

    def get_any_dicom(self):
        return random.choice(self.instances)
        