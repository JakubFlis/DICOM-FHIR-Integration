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
<<<<<<< HEAD

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
=======
        self.uid = parameters[0]
        self.accession = parameters[1]
        self.identifier = parameters[2]
        self.availability = parameters[3]
        self.modalityList = parameters[4]
        self.patient = parameters[5]
        self.context = parameters[6]
        self.started = parameters[7]
        self.basedOn = parameters[8]
        self.referrer = parameters[9]
        self.interpreter = parameters[10]
        self.endpoint = parameters[11]
        self.numberOfSeries = parameters[12]
        self.numberOfInstances = parameters[13]
        self.procedureReference = parameters[14]
        self.procedureCode = parameters[15]
        self.reason = parameters[16]
        self.description = parameters[17]
>>>>>>> 627ce2dc19d87e382562bee373981a0f4ba75d00
        self.series = series

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