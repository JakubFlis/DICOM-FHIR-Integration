""" 
More details about ImagingStudy object: https://www.hl7.org/fhir/imagingstudy.html
DICOM mapping table: https://www.hl7.org/fhir/imagingstudy-mappings.html

get_instance_title() method needs some correction. FHIR's title definition is in comments below.
"""

from Models.ImagingManifest import IMAGINGMANIFEST

from Models.InstanceManifest import INSTANCE
from Models.SeriesManifest import SERIES
from Models.StudyManifest import STUDY


def dcm_to_imaging_manifest(dicom_file):
    parameters = [None] * 6

    try:
        parameters[IMAGINGMANIFEST.IDENTIFIER] = dicom_file[0x08, 0x18].value  # Obligatory in FHIR
    except KeyError:
        print "Input file doesn't contain essential (0008,0018) tag."
        parameters[IMAGINGMANIFEST.IDENTIFIER] = None
        pass

    try:
        parameters[IMAGINGMANIFEST.PATIENT] = dicom_file[0x10, 0x20].value
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

    try:
        parameters[IMAGINGMANIFEST.STUDY] = dicom_file[0x40, 0xA160].value
    except KeyError:
        pass


    return parameters


# FHIR's definition of title in DICOM mapping section:
#    title = (0070,0080) | (0040,A043) > (0008,0104) | (0042,0010) | (0008,0008)
# What actually means:
#    title = ContentLabel | ConceptNameCodeSequence > CodeMeaning | DocumentTitle | ImageType

def dcm_to_study_manifest(dicom_file):
    parameters = [None] * 4
    try:
        parameters[STUDY.UID] = dicom_file[0x20, 0x0D].value
    except KeyError:
        print "Input file doesn't contain essential (0020,000D) tag."
        parameters[STUDY.UID] = None
        pass

    try:
        parameters[STUDY.ENDPOINT] = None
    except KeyError:
        pass


    return parameters


def dcm_to_series_manifest(dicom_file):
    parameters = [None] * 2

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
    parameters = [None] * 2

   # try:
    #    parameters[INSTANCE.SOPCLASS] = dicom_file[0x08, 0x16].value
   # except KeyError:
   #     pass

    try:
        parameters[INSTANCE.UID] = dicom_file[0x08, 0x18].value
    except KeyError:
        pass

    return parameters