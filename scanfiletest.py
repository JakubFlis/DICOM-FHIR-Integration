import os

def makePatients(rootDir):
    for patientDir in os.listdir(rootDir):
        if not os.path.isfile(os.path.join(rootDir, patientDir)):
            print "Found a patient at", patientDir
            makeStudy(rootDir + patientDir)

def makeStudy(patientDir):
    for studyDir in os.listdir(patientDir):
        if not os.path.isfile(os.path.join(patientDir, studyDir)):
            print "    Found a study at", studyDir
            makeSeries(patientDir + '/' +  studyDir)

def makeSeries(studyDir):
    for seriesDir in os.listdir(studyDir):
        if not os.path.isfile(os.path.join(studyDir, seriesDir)):
            print "        Found a series at", seriesDir
            makeInstances(studyDir + '/' + seriesDir)

def makeInstances(seriesDir):
    for instanceDir in os.listdir(seriesDir):
        if os.path.isfile(os.path.join(seriesDir, instanceDir)) and not instanceDir[0] == '.':
            print "          * Found an instance at", instanceDir

makePatients('./Integration/DicomFolder/')