"""
This class is both used in ImagingStudy and ImagingManifest
In ImagingManifest it does not use all the parameters(only uid, instance, endpoint)
Initializing the class:
instanceParams = {INSTANCE.TITLE: 'some title', INSTANCE.UID: 'some uid'}
instance = Instance(instanceParams)
seriesParams = {SERIES.UID: 'some uid', SERIES.ENDPOINT: 'some endpoint'}
series = Series(seriesParams, instance)
"""


class SeriesManifest:
    def __init__(self, parameters):
        self.uid = parameters[SERIES.UID]
        self.endpoint = parameters[SERIES.ENDPOINT]



class SERIES(object):
    UID = 0
    ENDPOINT = 1

