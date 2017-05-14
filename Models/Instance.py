"""
This class is both used in ImagingStudy and ImagingManifest
In ImagingManifest it does not use all the parameters(only uid, sopClass)
Initializing the class:
instanceParams = {INSTANCE.TITLE: 'some title', INSTANCE.UID: 'some uid'}
instance = Instance(instanceParams)
"""


class Instance:
	def __init__(self, parameters):
		self.uid = parameters[INSTANCE.UID]
		self.number = parameters[INSTANCE.NUMBER]
		self.sopClass = parameters[INSTANCE.SOPCLASS]
		self.title = parameters[INSTANCE.TITLE]


class INSTANCE(object):
	UID = 0
	NUMBER = 1
	SOPCLASS = 2
	TITLE = 3
