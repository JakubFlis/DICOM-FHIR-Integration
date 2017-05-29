""" 
More details about ImagingStudy object: https://www.hl7.org/fhir/imagingstudy.html
DICOM mapping table: https://www.hl7.org/fhir/imagingstudy-mappings.html

get_instance_title() method needs some correction. FHIR's title definition is in comments below.
"""
from Models.ImagingStudy import IMAGINGSTUDY, ImagingStudy
from DicomProcessor import DicomProcessor
from SeriesProcessor import SeriesProcessor

class ImagingStudyProcessor(DicomProcessor):
    def process_dicom_file(self):
        parameters = dict()
        processing_configs = [
            {
                'parameterName': IMAGINGSTUDY.UID,
                'dicomTagCoordinates': [0x20, 0x0D]
            },
            {
                'parameterName': IMAGINGSTUDY.ACCESSION,
                'dicomTagCoordinates': [0x08, 0x50]
            },
            {
                'parameterName': IMAGINGSTUDY.IDENTIFIER,
                'dicomTagCoordinates': [0x20, 0x10]
            },
            {
                'parameterName': IMAGINGSTUDY.MODALITYLIST,
                'dicomTagCoordinates': [0x08, 0x61]
            },
            {
                'parameterName': IMAGINGSTUDY.INTERPRETER,
                'dicomTagCoordinates': [0x08, 0x1060]
            },
            {
                'parameterName': IMAGINGSTUDY.NUMBEROFSERIES,
                'dicomTagCoordinates': [0x20, 0x1206]
            },
            {
                'parameterName': IMAGINGSTUDY.NUMBEROFINSTANCES,
                'dicomTagCoordinates': [0x20, 0x1208]
            },
            {
                'parameterName': IMAGINGSTUDY.PROCEDUREREFERENCE,
                'dicomTagCoordinates': [0x08, 0x1032]
            },
            {
                'parameterName': IMAGINGSTUDY.DESCRIPTION,
                'dicomTagCoordinates': [0x08, 0x1030]
            }
        ]

        for processing_config in processing_configs:
            failure_callback = None
            if processing_config['parameterName'] == IMAGINGSTUDY.UID:
                failure_callback = self.obligatory_parameter_failure_callback
            self.process_dicom_tag(parameters, processing_config['parameterName'], processing_config['dicomTagCoordinates'], failure_callback)

        parameters[IMAGINGSTUDY.AVAILABILITY] = None  # Unsupported by DICOM
        parameters[IMAGINGSTUDY.PATIENT] = None  # Obligatory in FHIR
        parameters[IMAGINGSTUDY.CONTEXT] = None  # Reference(Encounter | EpisodeOfCare)
        parameters[IMAGINGSTUDY.BASEDON] = None  # Reference(ReferralRequest | CarePlan | ProcedureRequest)
        parameters[IMAGINGSTUDY.REFERRER] = None  # Reference(Practitioner)
        parameters[IMAGINGSTUDY.ENDPOINT] = None  # Reference(Endpoint)
        parameters[IMAGINGSTUDY.PROCEDURECODE] = None  # ?
        parameters[IMAGINGSTUDY.REASON] = None  # ?

        try:
            # StudyDate (YYYYMMDD) + StudyTime (hhmmss.dddddd)
            parameters[IMAGINGSTUDY.STARTED] = (self.dicom_file[0x08, 0x20].value + self.dicom_file[0x08, 0x30].value)
        except KeyError:
            pass
        print "Finished mapping ImagingStudy instance."

        return ImagingStudy(parameters, SeriesProcessor(self.dicom_file).process_dicom_file())

    def process_dicom_tag(self, parameters, parameterName, dicomTagCoordinates, failureCallback):
        try:
            parameters[parameterName] = self.dicom_file[dicomTagCoordinates].value
        except KeyError:
            parameters[parameterName] = None
            pass

    def obligatory_parameter_failure_callback(self):
        print "Input file doesn't contain an essential tag!"
