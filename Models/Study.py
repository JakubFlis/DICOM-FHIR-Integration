"""
Initializing the class:
instanceParams = {INSTANCE.TITLE: 'some title', INSTANCE.UID: 'some uid'}
instance = Instance(instanceParams)
seriesParams = {SERIES.UID: 'some uid', SERIES.ENDPOINT: 'some endpoint'}
series = Series(seriesParams, instance)
imagingStudyParams = {IMAGINGMSTUDY.UID: 'some uid', IMAGINGSTUDY.PATIENT: 'some patient'}
imagingStudy = ImagingStudy(imagingStudy, series)
studyParameters = {STUDY.UID: 'some uid', STUDY.IMAGINGSTUDY: 'uid of imagingstudy', STUDY.ENDPOINT: 'some endpoint'}
study = Study(studyParameters, imagingStudy, series)
"""
class Study:
    def __init__(self, parameters, imagingStudy, series):
        self.uid = parameters[STUDY.UID]
        self.imagingStudy = imagingStudy
        self.endpoint = parameters[STUDY.ENDPOINT]
        self.series = series

class STUDY(object):
    UID = 0
    ENDPOINT = 2
