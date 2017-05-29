from Models.Series import SERIES, Series
from Processors.DicomProcessor import DicomProcessor
from Processors.InstanceProcessor import InstanceProcessor

class SeriesProcessor(DicomProcessor):
    def process_dicom_file(self):
        parameters = dict()
        processing_configs = [
            {
                'parameterName': SERIES.UID,
                'dicomTagCoordinates': [0x20, 0x0E]
            },
            {
                'parameterName': SERIES.NUMBER,
                'dicomTagCoordinates': [0x20, 0x11]
            },
            {
                'parameterName': SERIES.MODALITY,
                'dicomTagCoordinates': [0x08, 0x60]
            },
            {
                'parameterName': SERIES.DESCRIPTION,
                'dicomTagCoordinates': [0x08, 0x103E]
            },
            {
                'parameterName': SERIES.NUMBEROFINSTANCES,
                'dicomTagCoordinates': [0x20, 0x1209]
            },
            {
                'parameterName': SERIES.AVAILABILITY,
                'dicomTagCoordinates': [0x08, 0x56]
            },
            {
                'parameterName': SERIES.BODYSITE,
                'dicomTagCoordinates': [0x18, 0x15]
            },
            {
                'parameterName': SERIES.LATERALITY,
                'dicomTagCoordinates': [0x20, 0x60]
            },
            {
                'parameterName': SERIES.PERFORMER,
                'dicomTagCoordinates': [0x08, 0x1050]
            }
        ]

        for processing_config in processing_configs:
            failure_callback = None
            if processing_config['parameterName'] == SERIES.UID:
                failure_callback = self.obligatory_parameter_failure_callback
            self.process_dicom_tag(parameters, processing_config['parameterName'], processing_config['dicomTagCoordinates'], failure_callback)

        parameters[SERIES.ENDPOINT] = None  # Reference(Endpoint)

        try:
            # SeriesDate (YYYYMMDD) + SeriesTime (hhmmss.dddddd)
            parameters[SERIES.STARTED] = (self.dicom_file[0x08, 0x21].value + self.dicom_file[0x08, 0x31].value)
        except KeyError:
            pass

        parameters[SERIES.INSTANCE] = InstanceProcessor(self.dicom_file).processDicomFile()

        print "Finished mapping Series instance."

        return Series(parameters)

    def process_dicom_tag(self, parameters, parameter_name, dicom_tag_coordinates, failure_callback):
        try:
            parameters[parameter_name] = self.dicom_file[dicom_tag_coordinates].value
        except KeyError:
            parameters[parameter_name] = None
            if failure_callback != None:
                failure_callback()

    def obligatory_parameter_failure_callback(self):
        print "Input file doesn't contain an essential tag!"
