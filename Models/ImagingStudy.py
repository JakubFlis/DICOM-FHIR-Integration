class ImagingStudy:

    def __init__(self, parameters, series):

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
        self.series = series
