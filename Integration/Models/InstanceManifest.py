"""
This class is both used in ImagingStudy and ImagingManifest
In ImagingManifest it does not use all the parameters(only uid, sopClass)
Initializing the class:
instanceParams = {INSTANCE.TITLE: 'some title', INSTANCE.UID: 'some uid'}
instance = Instance(instanceParams)
"""


class InstanceManifest:
    def __init__(self, parameters):
        self.uid = parameters[INSTANCE.UID]
      #  self.sopClass = parameters[INSTANCE.SOPCLASS]



class INSTANCE(object):
    UID = 0
   # SOPCLASS = 2

