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
imagingManifestParams = {IMAGINGMANIFEST.IDENTIFIER: 'some identifier', IMAGINGMANIFEST.PATIENT: 'some patient'}
imagingManifest = ImagingManifest(imagingManifestParams,study)
"""


class ImagingManifest:
	def __init__(self, parameters, study):
		self.identifier = parameters[IMAGINGMANIFEST.IDENTIFIER]
		self.patient = parameters[IMAGINGMANIFEST.PATIENT]
		self.authoringTime = parameters[IMAGINGMANIFEST.AUTHORINGTIME]
		self.author = parameters[IMAGINGMANIFEST.AUTHOR]
		self.description = parameters[IMAGINGMANIFEST.DESCRIPTION]
		self.study = study


class IMAGINGMANIFEST(object):
	IDENTIFIER = 0
	PATIENT = 1
	AUTHORINGTIME = 2
	AUTHOR = 3
	DESCRIPTION = 4
	STUDY = 5
