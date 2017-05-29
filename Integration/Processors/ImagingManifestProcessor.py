from Models.ImagingManifest import IMAGINGMANIFEST, ImagingManifest
from DicomProcessor import DicomProcessor
from StudyProcessor import StudyProcessor

class ImagingManifestProcessor(DicomProcessor):
    def process_dicom_file(self):
        parameters = dict()
        processing_configs = [
            {
                'parameterName': IMAGINGMANIFEST.IDENTIFIER,
                'dicomTagCoordinates': [0x20, 0x0D]
            },
            {
                'parameterName': IMAGINGMANIFEST.PATIENT,
                'dicomTagCoordinates': [0x08, 0x50]
            },
            {
                'parameterName': IMAGINGMANIFEST.AUTHORINGTIME,
                'dicomTagCoordinates': [0x20, 0x10]
            },
            {
                'parameterName': IMAGINGMANIFEST.AUTHOR,
                'dicomTagCoordinates': [0x08, 0x61]
            },
            {
                'parameterName': IMAGINGMANIFEST.DESCRIPTION,
                'dicomTagCoordinates': [0x08, 0x1060]
            }
        ]

        for processing_config in processing_configs:
            failure_callback = None
            if processing_config['parameterName'] == IMAGINGMANIFEST.IDENTIFIER:
                failure_callback = self.obligatory_parameter_failure_callback
            self.process_dicom_tag(parameters, processing_config['parameterName'], processing_config['dicomTagCoordinates'], failure_callback)

        parameters[IMAGINGMANIFEST.STUDY] = StudyProcessor(self.dicom_file).process_dicom_file()

        print "Finished mapping ImagingManifestProcessor"

        return ImagingManifest(parameters)

    def process_dicom_tag(self, parameters, parameter_name, dicom_tag_coordinates, failure_callback):
        try:
            parameters[parameter_name] = self.dicom_file[dicom_tag_coordinates].value
        except KeyError:
            parameters[parameter_name] = None
            if failure_callback != None:
                failure_callback()

    def obligatory_parameter_failure_callback(self):
        print "Input file doesn't contain an essential tag!"
