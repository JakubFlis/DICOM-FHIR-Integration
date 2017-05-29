"""
This class is both used in ImagingStudy and ImagingManifest
In ImagingManifest it does not use all the parameters(only uid, instance, endpoint)
Initializing the class:
instanceParams = {INSTANCE.TITLE: 'some title', INSTANCE.UID: 'some uid'}
instance = Instance(instanceParams)
seriesParams = {SERIES.UID: 'some uid', SERIES.ENDPOINT: 'some endpoint'}
series = Series(seriesParams, instance)
"""
class Series:
    def __init__(self, parameters):
        self.uid = parameters[SERIES.UID]
        self.number = parameters[SERIES.NUMBER]
        self.modality = parameters[SERIES.MODALITY]
        self.description = parameters[SERIES.DESCRIPTION]
        self.numberOfInstances = parameters[SERIES.NUMBEROFINSTANCES]
        self.availability = parameters[SERIES.AVAILABILITY]
        self.endpoint = parameters[SERIES.ENDPOINT]
        self.bodySite = parameters[SERIES.BODYSITE]
        self.laterality = parameters[SERIES.LATERALITY]
        self.started = parameters[SERIES.STARTED]
        self.performer = parameters[SERIES.PERFORMER]
        self.instance = parameters[SERIES.INSTANCE]

class SERIES(object):
    UID = 0
    NUMBER = 1
    MODALITY = 2
    DESCRIPTION = 3
    NUMBEROFINSTANCES = 4
    AVAILABILITY = 5
    ENDPOINT = 6
    BODYSITE = 7
    LATERALITY = 8
    STARTED = 9
    PERFORMER = 10
    INSTANCE = 11
