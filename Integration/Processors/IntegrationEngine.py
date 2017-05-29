import dicom
from ImagingStudyProcessor import ImagingStudyProcessor

class IntegrationEngine:
    def __init__(self, dcm_file_path):
        try:
            self.dicom_file = dicom.read_file(dcm_file_path)
        except IOError:
            print "There's no file under path", dcm_file_path

        ImagingStudyProcessor(self.dicom_file).process_dicom_file()