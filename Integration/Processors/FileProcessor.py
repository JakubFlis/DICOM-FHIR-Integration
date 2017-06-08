""" FileProcessor module """
import os

class FileProcessor(object):
    """ FileProcessor has methods for scanning the file tree and creating Folder and Instance objects """

    @staticmethod
    def make_patients(root_dir):
        for patient_dir in os.listdir(root_dir):
            if not os.path.isfile(os.path.join(root_dir, patient_dir)):
                print "Found a patient at", patient_dir
                FileProcessor.make_study(root_dir + patient_dir)

    @staticmethod
    def make_study(patient_dir):
        for study_dir in os.listdir(patient_dir):
            if not os.path.isfile(os.path.join(patient_dir, study_dir)):
                print "    Found a study at", study_dir
                FileProcessor.make_series(patient_dir + '/' +  study_dir)

    @staticmethod
    def make_series(study_dir):
        for series_dir in os.listdir(study_dir):
            if not os.path.isfile(os.path.join(study_dir, series_dir)):
                print "        Found a series at", series_dir
                FileProcessor.make_instances(study_dir + '/' + series_dir)

    @staticmethod
    def make_instances(series_dir):
        for instance_dir in os.listdir(series_dir):
            # We don't want to scan hidden files (.)
            if os.path.isfile(os.path.join(series_dir, instance_dir)) and not instance_dir[0] == '.':
                print "          * Found an instance at", instance_dir

#makePatients('./Integration/DicomFolder/')