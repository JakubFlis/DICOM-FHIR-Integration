"""
Initializing the class:
instanceParams = {INSTANCE.TITLE: 'some title', INSTANCE.UID: 'some uid'}
instance = Instance(instanceParams)
seriesParams = {SERIES.UID: 'some uid', SERIES.ENDPOINT: 'some endpoint'}
series = Series(seriesParams, instance)
imagingStudyParams = {IMAGINGMSTUDY.UID: 'some uid', IMAGINGSTUDY.PATIENT: 'some patient'}
imagingStudy = ImagingStudy(imagingStudy, series)
"""
class ImagingStudy:
    def __init__(self, parameters, series):
        self.uid = parameters[IMAGINGSTUDY.UID]
        self.accession = parameters[IMAGINGSTUDY.ACCESSION]
        self.identifier = parameters[IMAGINGSTUDY.IDENTIFIER]
        self.availability = parameters[IMAGINGSTUDY.AVAILABILITY]
        self.modalityList = parameters[IMAGINGSTUDY.MODALITYLIST]
        self.patient = parameters[IMAGINGSTUDY.PATIENT]
        self.context = parameters[IMAGINGSTUDY.CONTEXT]
        self.started = parameters[IMAGINGSTUDY.STARTED]
        self.basedOn = parameters[IMAGINGSTUDY.BASEDON]
        self.referrer = parameters[IMAGINGSTUDY.REFERRER]
        self.interpreter = parameters[IMAGINGSTUDY.INTERPRETER]
        self.endpoint = parameters[IMAGINGSTUDY.ENDPOINT]
        self.numberOfSeries = parameters[IMAGINGSTUDY.NUMBEROFSERIES]
        self.numberOfInstances = parameters[IMAGINGSTUDY.NUMBEROFINSTANCES]
        self.procedureReference = parameters[IMAGINGSTUDY.PROCEDUREREFERENCE]
        self.procedureCode = parameters[IMAGINGSTUDY.PROCEDURECODE]
        self.reason == parameters[IMAGINGSTUDY.REASON]
        self.description = parameters[IMAGINGSTUDY.DESCRIPTION]

class IMAGINGSTUDY(object):
    UID = 0
    ACCESSION = 1
    IDENTIFIER = 2
    AVAILABILITY = 3
    MODALITYLIST = 4
    PATIENT = 5
    CONTEXT = 6
    STARTED = 7
    BASEDON = 8
    REFERRER = 9
    INTERPRETER = 10
    ENDPOINT = 11
    NUMBEROFSERIES = 12
    NUMBEROFINSTANCES = 13
    PROCEDUREREFERENCE = 14
    PROCEDURECODE = 15
    REASON = 16
    DESCRIPTION = 17