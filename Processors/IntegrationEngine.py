#!/usr/bin/python

import dicom

class IntegrationEngine():
    def __init__(self, dicomFilePath):
        self.dicomFile = dicom.read_file(dicomFilePath)