#!/usr/bin/python

import dicom

class IntegrationEngine:
    def __init__(self, dicomFilePath):
        try:
            self.dicomFile = dicom.read_file(dicomFilePath)
        except IOError:
            print "There's no file under path", dicomFilePath
        