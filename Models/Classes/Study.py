class Study:
    def __init__(self, parameters, series):
        self.uid = parameters[0]
        self.imagingStudy = parameters[1]
        self.endpoint = parameters[2]
        self.series = series
