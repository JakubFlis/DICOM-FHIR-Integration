""" 
More details about ImagingStudy object: https://www.hl7.org/fhir/imagingstudy.html
DICOM mapping table: https://www.hl7.org/fhir/imagingstudy-mappings.html

get_instance_title() method needs some correction. FHIR's title definition is in comments below.
"""

from Models.ImagingStudy import IMAGINGSTUDY
from Models.Series import SERIES
from Models.Instance import INSTANCE


def dcm_to_imaging_study(dicom_file):
    parameters = [None] * 18

    try:
        parameters[IMAGINGSTUDY.UID] = dicom_file[0x20, 0x0D].value  # Obligatory in FHIR
    except KeyError:
        print "Input file doesn't contain essential (0020,000D) tag."
        parameters[IMAGINGSTUDY.UID] = None
        pass

    try:
        parameters[IMAGINGSTUDY.ACCESSION] = dicom_file[0x08, 0x50].value
    except KeyError:
        pass

    try:
        parameters[IMAGINGSTUDY.IDENTIFIER] = dicom_file[0x20, 0x10].value
    except KeyError:
        pass

    parameters[IMAGINGSTUDY.AVAILABILITY] = None  # Unsupported by DICOM

    try:
        parameters[IMAGINGSTUDY.MODALITYLIST] = dicom_file[0x08, 0x61].value
    except KeyError:
        pass

    # TODO: Reference(Patient) (with 0010/* tags) ???
    parameters[IMAGINGSTUDY.PATIENT] = None  # Obligatory in FHIR

    parameters[IMAGINGSTUDY.CONTEXT] = None  # Reference(Encounter | EpisodeOfCare)

    try:
        # StudyDate (YYYYMMDD) + StudyTime (hhmmss.dddddd)
        parameters[IMAGINGSTUDY.STARTED] = (dicom_file[0x08, 0x20].value + dicom_file[0x08, 0x30].value)
    except KeyError:
        pass

    parameters[IMAGINGSTUDY.BASEDON] = None  # Reference(ReferralRequest | CarePlan | ProcedureRequest)
    parameters[IMAGINGSTUDY.REFERRER] = None  # Reference(Practitioner)

    try:
        parameters[IMAGINGSTUDY.INTERPRETER] = dicom_file[0x08, 0x1060].value
    except KeyError:
        pass

    parameters[IMAGINGSTUDY.ENDPOINT] = None  # Reference(Endpoint)

    try:
        parameters[IMAGINGSTUDY.NUMBEROFSERIES] = dicom_file[0x20, 0x1206].value
    except KeyError:
        pass

    try:
        parameters[IMAGINGSTUDY.NUMBEROFINSTANCES] = dicom_file[0x20, 0x1208].value
    except KeyError:
        pass

    try:
        parameters[IMAGINGSTUDY.PROCEDUREREFERENCE] = dicom_file[0x08, 0x1032].value
    except KeyError:
        pass

    parameters[IMAGINGSTUDY.PROCEDURECODE] = None  # ?
    parameters[IMAGINGSTUDY.REASON] = None  # ?

    try:
        parameters[IMAGINGSTUDY.DESCRIPTION] = dicom_file[0x08, 0x1030].value
    except KeyError:
        pass

    return parameters


# FHIR's definition of title in DICOM mapping section:
#    title = (0070,0080) | (0040,A043) > (0008,0104) | (0042,0010) | (0008,0008)
# What actually means:
#    title = ContentLabel | ConceptNameCodeSequence > CodeMeaning | DocumentTitle | ImageType
def get_instance_title(dicom_file):
    title = 'Title: '
    try:
        title = dicom_file[0x07, 0x80].value  # ContentLabel
    except KeyError:
        pass

    try:
        title = dicom_file[0x40, 0xA043].value  # ConceptNameCodeSequence
    except KeyError:
        pass

    try:
        title = dicom_file[0x08, 0x0104].value  # CodeMeaning`
    except KeyError:
        pass

    try:
        title = dicom_file[0x42, 0x10].value  # DocumentTitle
    except KeyError:
        pass

    try:
        title = dicom_file[0x08, 0x08].value  # ImageType
    except KeyError:
        pass

    return title


def dcm_to_instance(dicom_file):
    parameters = [None] * 4
    try:
        parameters[INSTANCE.UID] = dicom_file[0x08, 0x18].value
    except KeyError:
        print "Input file doesn't contain essential (0008,0018) tag."
        parameters[INSTANCE.UID] = None
        pass

    try:
        parameters[INSTANCE.NUMBER] = dicom_file[0x20, 0x13].value
    except KeyError:
        pass

    try:
        parameters[INSTANCE.SOPCLASS] = dicom_file[0x08, 0x16].value
    except KeyError:
        pass

    try:
        parameters[INSTANCE.TITLE] = get_instance_title(dicom_file)
    except KeyError:
        pass

    return parameters


def dcm_to_series(dicom_file):
    parameters = [None] * 11

    try:
        parameters[SERIES.UID] = dicom_file[0x20, 0x0E].value
    except KeyError:
        print "Input file doesn't contain essential (0020,000E) tag."
        parameters[SERIES.UID] = None
        pass

    try:
        parameters[SERIES.NUMBER] = dicom_file[0x20, 0x11].value
    except KeyError:
        pass

    try:
        parameters[SERIES.MODALITY] = dicom_file[0x08, 0x60].value
    except KeyError:
        pass

    try:
        parameters[SERIES.DESCRIPTION] = dicom_file[0x08, 0x103E].value
    except KeyError:
        pass

    try:
        parameters[SERIES.NUMBEROFINSTANCES] = dicom_file[0x20, 0x1209].value
    except KeyError:
        pass

    try:
        parameters[SERIES.AVAILABILITY] = dicom_file[0x08, 0x56].value
    except KeyError:
        pass

    parameters[SERIES.ENDPOINT] = None  # Reference(Endpoint)

    try:
        parameters[SERIES.BODYSITE] = dicom_file[0x18, 0x15].value
    except KeyError:
        pass

    try:
        parameters[SERIES.LATERALITY] = dicom_file[0x20, 0x60].value
    except KeyError:
        pass

    try:
        # SeriesDate (YYYYMMDD) + SeriesTime (hhmmss.dddddd)
        parameters[SERIES.STARTED] = (dicom_file[0x08, 0x21].value + dicom_file[0x08, 0x31].value)
    except KeyError:
        pass

    try:
        performer = dicom_file[0x08, 0x1050].value
    except KeyError:
        try:
            performer = dicom_file[0x08, 0x1072].value
        except KeyError:
            performer = None
    parameters[SERIES.PERFORMER] = performer

    return parameters
