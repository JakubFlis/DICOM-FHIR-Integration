from Models.Instance import INSTANCE, Instance
from Processors.DicomProcessor import DicomProcessor

class InstanceProcessor(DicomProcessor):
    def processDicomFile(self):
        parameters = dict()
        processing_configs = [
            {
                'parameterName': INSTANCE.UID,
                'dicomTagCoordinates': [0x08, 0x18]
            },
            {
                'parameterName': INSTANCE.NUMBER,
                'dicomTagCoordinates': [0x20, 0x13]
            },
            {
                'parameterName': INSTANCE.SOPCLASS,
                'dicomTagCoordinates': [0x08, 0x16]
            },
            {
                'parameterName': INSTANCE.TITLE,
                'dicomTagCoordinates': [0x07, 0x80]
            }
        ]

        for processing_config in processing_configs:
            failure_callback = None
            if processing_config['parameterName'] == INSTANCE.UID:
                failure_callback = self.obligatory_parameter_failure_callback
            self.process_dicom_tag(parameters, processing_config['parameterName'], processing_config['dicomTagCoordinates'], failure_callback)

        print "Finished mapping Instance object."

        return Instance(parameters)

    def process_dicom_tag(self, parameters, parameter_name, dicom_tag_coordinates, failure_callback):
        try:
            parameters[parameter_name] = self.dicom_file[dicom_tag_coordinates].value
        except KeyError:
            parameters[parameter_name] = None
            if failure_callback != None:
                failure_callback()

    def obligatory_parameter_failure_callback(self):
        print "Input file doesn't contain an essential tag!"
        