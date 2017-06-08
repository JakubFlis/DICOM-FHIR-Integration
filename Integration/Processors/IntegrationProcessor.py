""" IntegrationProcessor module """
from Processors.FileProcessor import FileProcessor
from Processors.ConfigProcessor import ConfigProcessor

class IntegrationProcessor(object):
    """ This class manages other processors into one integration pipeline. """

    def __init__(self, config_path, root_path):
        self.config_path = config_path
        self.root_path = root_path

    def integrate(self):
        patients = FileProcessor.make_patients(self.root_path)
        print ConfigProcessor("<template_file_path>", patients).render_template()