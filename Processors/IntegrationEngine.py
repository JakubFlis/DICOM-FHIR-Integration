#!/usr/bin/python

import dicom

class IntegrationEngine:
    def __init__(self, dicomFilePath):
        try:
            self.dicomFile = dicom.read_file(dicomFilePath)
        except IOError:
            print "There's no file under path", dicomFilePath
        print "(0008,0070) = ", self.dicomFile[0x08, 0x70].value