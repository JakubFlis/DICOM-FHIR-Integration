class Series:
    def __init__(self, parameters, instance):
        self.uid = parameters[0]
        self.number = parameters[1]
        self. modality = parameters[2]
        self.description = parameters[3]
        self.numberOfInstances = parameters[4]
        self.availability = parameters[5]
        self.endpoint = parameters[6]
        self. bodySite = parameters[7]
        self.laterality = parameters[8]
        self.started = parameters[9]
        self.performer = parameters[10]
        self.instance = instance