class ImagingManifest:
    def __init__(self, parameters, study):
        self.identifier = parameters[0]
        self.patient = parameters[1]
        self.authoringTime = parameters[2]
        self.author = parameters[3]
        self.description = parameters[4]
        self.study = study
