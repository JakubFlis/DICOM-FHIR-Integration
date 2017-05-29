from Models.Study import STUDY, Study
from DicomProcessor import DicomProcessor
from ImagingStudyProcessor import ImagingStudyProcessor

class StudyProcessor(DicomProcessor):
    def process_dicom_file(self):
        parameters = dict()
        processing_configs = [
            {
                'parameterName': STUDY.UID,
                'dicomTagCoordinates': [0x20, 0x0D]
            }
        ]

        for processing_config in processing_configs:
            failure_callback = None
            if processing_config['parameterName'] == STUDY.UID:
                failure_callback = self.obligatory_parameter_failure_callback
            self.process_dicom_tag(parameters, processing_config['parameterName'], processing_config['dicomTagCoordinates'], failure_callback)

        parameters[STUDY.ENDPOINT] = None #?
        parameters[STUDY.IMAGINGSTUDY] = ImagingStudyProcessor(self.dicom_file).process_dicom_file()

        print "Finished mapping Study object."

        return Study(parameters)

    def process_dicom_tag(self, parameters, parameter_name, dicom_tag_coordinates, failure_callback):
        try:
            parameters[parameter_name] = self.dicom_file[dicom_tag_coordinates].value
        except KeyError:
            parameters[parameter_name] = None
            if failure_callback != None:
                failure_callback()

    def obligatory_parameter_failure_callback(self):
        print "Input file doesn't contain an essential tag!"
