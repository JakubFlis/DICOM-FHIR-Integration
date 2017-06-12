""" Instance module """
import dicom
from Folder import Folder

class Instance(object):
    """ This class represents an Instace file (DICOM), that is inside a Series folder. """

    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        try:
            self.dicom_file = dicom.read_file(path_to_file)
        except IOError:
            print "There's no file under path", path_to_file

    def read_property(self, coord_x, coord_y):
        """ Reads the DICOM file with given coordinates and
        returns a string with its content. """
        result = None
        try:
            result = self.dicom_file[int(coord_x, 16), int(coord_y, 16)].value
        except KeyError:
            pass
        except ValueError:
            raise Exception("Please check coordinates of the DICOM file.")

        return result
