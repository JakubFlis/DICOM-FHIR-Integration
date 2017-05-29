from Models.Instance import INSTANCE, Instance
from Processors.DicomProcessor import DicomProcessor

class InstanceProcessor(DicomProcessor):
    def processDicomFile(self):
        parameters = dict()
        processingConfigs = [
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

        for processingConfig in processingConfigs:
            failureCallback = None
            if processingConfig['parameterName'] == INSTANCE.UID:
                failureCallback = self.obligatoryParameterFailureCallback
            self.processDicomTag(parameters, processingConfig['parameterName'], processingConfig['dicomTagCoordinates'], failureCallback)

        print "Finished mapping Instance object."

        return Instance(parameters)

    def processDicomTag(self, parameters, parameterName, dicomTagCoordinates, failureCallback):
        try:
            parameters[parameterName] = self.dicom_file[dicomTagCoordinates].value
        except KeyError:
            parameters[parameterName] = None

    def obligatoryParameterFailureCallback(self, tagName):
        print "Input file doesn't contain an essential tag!"
        