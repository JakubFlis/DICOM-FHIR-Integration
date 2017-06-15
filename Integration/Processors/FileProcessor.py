""" FileProcessor module """
import os
import sys
from Models.Instance import Instance
from Models.Series import Series
from Models.Study import Study
from Models.Patient import Patient

class FileProcessor(object):
    """ FileProcessor has methods for scanning the file tree and creating Folder and Instance objects """
    file_counter = 0

    def make_patients(self, root_dir):
        patients = []
        for patient_dir in os.listdir(root_dir):
            if not os.path.isfile(os.path.join(root_dir, patient_dir)):
                patients.append(Patient(self.make_study(root_dir + '/' + patient_dir), patient_dir))
        print "\nFinished processing the folder structure."
        return patients

    def make_study(self, patient_dir):
        studies = []
        for study_dir in os.listdir(patient_dir):
            if not os.path.isfile(os.path.join(patient_dir, study_dir)):
                studies.append(Study(self.make_series(patient_dir + '/' +  study_dir), study_dir))
        return studies

    def make_series(self, study_dir):
        series = []
        for series_dir in os.listdir(study_dir):
            if not os.path.isfile(os.path.join(study_dir, series_dir)):
                series.append(Series(self.make_instances(study_dir + '/' + series_dir), series_dir))
        return series

    def make_instances(self, series_dir):
        instances = []
        for instance_dir in os.listdir(series_dir):
            # We don't want to scan hidden files (.)
            if os.path.isfile(os.path.join(series_dir, instance_dir)) and not instance_dir[0] == '.':
                instances.append(Instance(series_dir + '/' + instance_dir))
                self.update_progress_bar()
        return instances

    def update_progress_bar(self):
        self.file_counter += 1
        sys.stdout.write("\r%d" % self.file_counter + " - number of processed DICOM files")
        sys.stdout.flush()