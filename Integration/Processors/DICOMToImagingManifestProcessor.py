""" 
More details about ImagingManifest object: https://www.hl7.org/fhir/imagingmanifest.html
DICOM mapping table: https://www.hl7.org/fhir/imagingstudy-mappings.html

TODO - Study - imagingStudy (0020,000D) - Study Instance UID
"""

from Models.ImagingManifest import IMAGINGMANIFEST
from Models.Instance import INSTANCE
from Models.Series import SERIES
from Models.Study import STUDY


def dcm_to_imaging_manifest(dicom_file):
    parameters = [None] * 6

    try:
        parameters[IMAGINGMANIFEST.IDENTIFIER] = dicom_file[0x08, 0x18].value  # Obligatory in FHIR
    except KeyError:
        print "Input file doesn't contain essential (0008,0018) tag."
        parameters[IMAGINGMANIFEST.IDENTIFIER] = None
        pass

    try:
        parameters[IMAGINGMANIFEST.PATIENT] = get_instance_patient(dicom_file)
    except KeyError:
        pass

    try:
        parameters[IMAGINGMANIFEST.AUTHORINGTIME] = dicom_file[0x40, 0xA032].value
    except KeyError:
        pass

    try:
        parameters[IMAGINGMANIFEST.AUTHOR] = dicom_file[0x40, 0xA730].value
    except KeyError:
        pass

    try:
        parameters[IMAGINGMANIFEST.DESCRIPTION] = dicom_file[0x40, 0xA160].value
    except KeyError:
        pass

    return parameters


def get_instance_patient(dicom_file):

    try:
        patientName = dicom_file[0x10, 0x10].value
    except KeyError:
        patientName = ''
        pass

    try:
        patientID = ' ' + dicom_file[0x10, 0x20].value
    except KeyError:
        patientID = ''
        pass

    try:
        issuerOfPatientID = ' ' + dicom_file[0x10, 0x21].value
    except KeyError:
        issuerOfPatientID = ''
        pass

    patient = patientName +  patientID  + issuerOfPatientID

    return patient


def dcm_to_study_manifest(dicom_file):
    parameters = [None] * 6
    try:
        parameters[STUDY.UID] = dicom_file[0x20, 0x0D].value
    except KeyError:
        print "Input file doesn't contain essential (0020,000D) tag."
        parameters[STUDY.UID] = None
        pass

## TODO Study imagingStudy (0020,000D) - Study Instance UID


    try:
        parameters[STUDY.ENDPOINT] = None
    except KeyError:
        pass


    return parameters


def dcm_to_series_manifest(dicom_file):
    parameters = [None] * 11

    try:
        parameters[SERIES.UID] = dicom_file[0x20, 0x0E].value
    except KeyError:
        print "Input file doesn't contain essential (0020,000E) tag."
        parameters[SERIES.UID] = None
        pass

    try:
        parameters[SERIES.ENDPOINT] = None
    except KeyError:
        pass

    return parameters


def dcm_to_instance_manifest(dicom_file):
    parameters = [None] * 4

    try:
        parameters[INSTANCE.SOPCLASS] = dicom_file[0x08, 0x16].value
    except KeyError:
        pass

    try:
        parameters[INSTANCE.UID] = dicom_file[0x08, 0x18].value
    except KeyError:
        pass

    return parameters