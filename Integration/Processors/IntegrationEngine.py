#!/usr/bin/python

import dicom
from Models.ImagingStudy import ImagingStudy
from Models.Series import Series
from Models.Instance import Instance
from Models.ImagingManifest import ImagingManifest
from Models.Study import Study

from Processors.DICOMProcessor import dcm_to_imaging_study, dcm_to_series, dcm_to_instance
from Processors.DICOMToImagingManifestProcessor import dcm_to_imaging_manifest, dcm_to_instance_manifest, dcm_to_series_manifest, dcm_to_study_manifest


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

        manifest_instance_parameters = dcm_to_instance_manifest(self.dicom_file)
        manifest_instance = Instance(manifest_instance_parameters)

        manifest_series_parameters = dcm_to_series_manifest(self.dicom_file)
        manifest_series = Series(manifest_series_parameters, manifest_instance)

        manifest_study_parameters = dcm_to_study_manifest(self.dicom_file)
        manifest_study = Study(manifest_study_parameters, imaging_study, manifest_series)

        im_man_parameters = dcm_to_imaging_manifest(self.dicom_file)
        imaging_manifest = ImagingManifest(im_man_parameters, manifest_study)

        # Debug for created object
        print "imaging_study.uid = ", imaging_study.uid
        print "imaging_study.accession = ", imaging_study.accession
        print "imaging_study.identifier = ", imaging_study.identifier
        print "series.started = ", series.started
        print "instance.title = ", instance.title


        print "imaging_manifest.identifier = ", imaging_manifest.identifier
        print "imaging_manifest.patient = ", imaging_manifest.patient
        print "imaging_manifest.study.imagingStudy = ", manifest_study.imagingStudy  # Don't know what exactly should it print
        print "imaging_manifest.instance.sopclass = ", manifest_instance.sopClass
        print "imaging_manifest.series.uid = ", manifest_series.uid


