"""
Initializing the class:
instanceParams = {INSTANCE.TITLE: 'some title', INSTANCE.UID: 'some uid'}
instance = Instance(instanceParams)
seriesParams = {SERIES.UID: 'some uid', SERIES.ENDPOINT: 'some endpoint'}
series = Series(seriesParams, instance)
imagingStudyParams = {IMAGINGSTUDY.UID: 'some uid', IMAGINGSTUDY.PATIENT: 'some patient'}
imagingStudy = ImagingStudy(imagingStudy, series)
studyParameters = {STUDY.UID: 'some uid', STUDY.IMAGINGSTUDY: 'uid of imagingstudy', STUDY.ENDPOINT: 'some endpoint'}
study = Study(studyParameters, imagingStudy, series)
"""
class Study:
    def __init__(self, parameters):
        self.uid = parameters[STUDY.UID]
        self.imaging_study = parameters[STUDY.IMAGINGSTUDY]
        self.endpoint = parameters[STUDY.ENDPOINT]

class STUDY(object):
    UID = 0
    IMAGINGSTUDY = 1
    ENDPOINT = 2
