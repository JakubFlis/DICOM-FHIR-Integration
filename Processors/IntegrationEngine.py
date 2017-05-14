#!/usr/bin/python

import dicom
from Models.ImagingStudy import ImagingStudy
from Models.Series import Series
from Models.Instance import Instance
from Processors.DICOMProcessor import dcm_to_imaging_study, dcm_to_series, dcm_to_instance


class IntegrationEngine:
	def __init__(self, dcm_file_path):
		try:
			self.dicom_file = dicom.read_file(dcm_file_path)
		except IOError:
			print "There's no file under path", dcm_file_path

		instance_parameters = dcm_to_instance(self.dicom_file)
		instance = Instance(instance_parameters)

		series_parameters = dcm_to_series(self.dicom_file)
		series = Series(series_parameters, instance)

		im_st_parameters = dcm_to_imaging_study(self.dicom_file)
		imaging_study = ImagingStudy(im_st_parameters, series)

		# Debug for created object
		print "imaging_study.uid = ", imaging_study.uid
		print "imaging_study.accession = ", imaging_study.accession
		print "imaging_study.identifier = ", imaging_study.identifier
		print "series.started = ", series.started
		print "instance.title = ", instance.title
