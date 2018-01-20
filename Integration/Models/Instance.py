""" Instance module """
import dicom
from Folder import Folder

class Instance(object):
    """ This class represents an Instace file (DICOM), that is inside a Series folder. """
    SR_CONCEPT_NAME_CODE_SEQUENCE_VALUE = "Concept Name Code Sequence"
    SR_SEQUENCE_ELEMENT_TEXT_VALUE = "Text Value"
    
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        try:
            self.dicom_file = dicom.read_file(path_to_file)
        except IOError:
            print "There's no file under path", path_to_file

    def read_property(self, coord_x, coord_y):
        """ Reads the DICOM file with given coordinates and
        returns a string with its content. """ 
        result = ""
        try:
            result = self.dicom_file[int(coord_x, 16), int(coord_y, 16)].value
        except KeyError:
            pass
        except ValueError:
            raise Exception("Please check coordinates of the DICOM file.")

        return result

    def read_report_as_HTML(self, report_coords, header_coords):
        """ Reads a DICOM SR report sequence under given coordinates and returns as a string.
        @param report_coords - a string tuple with coords for the DICOM SR report sequence. Usually ("0x40", "0xa730").
        @param header_coords - a string tuple with coords for the DICOM SR header. Usually  ("0x08", "0x104")."""
        sequence = self.read_property(report_coords[0], report_coords[1])
        result = ""

        for element in sequence:
            for symbol in element:
                if symbol.name == self.SR_CONCEPT_NAME_CODE_SEQUENCE_VALUE:
                    for subsymbol in symbol:
                        result += "<b>"
                        result += subsymbol[int(header_coords[0], 16), int(header_coords[1], 16)].value
                        result += "</b> "

                if symbol.name == self.SR_SEQUENCE_ELEMENT_TEXT_VALUE:
                    result += "<p>"
                    result += symbol.value.encode('utf-8').strip().replace('"', '\\"').replace('\n', '\\n')
                    result += "</p>"

        return result
