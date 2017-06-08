""" Folder module """

class Folder(object):
    """ This is a superclass for all objects that are representing etiher a
    folder (Study, Series) or a DICOM File (Instance) """
    def get_any_dicom(self):
        """ This is an abstract method for searching for any DICOM file (Instance object)
        within a Folder """
        raise NotImplementedError
