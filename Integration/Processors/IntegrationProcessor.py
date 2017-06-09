""" IntegrationProcessor module """
from Processors.FileProcessor import FileProcessor
from Processors.ConfigProcessor import ConfigProcessor

class IntegrationProcessor(object):
    """ This class manages other processors into one integration pipeline. """

    def __init__(self, config_path, root_path):
        self.config_path = config_path
        self.root_path = root_path

    def integrate(self):
        """ Main integrating function. Binds FileProcessor and ConfigProcessor together.
        First, an array of patients is being made based on what is inside the folder under the given path.
        Then, the ConfigProcessor parses the template from the given path and renders the output. """
        patients = FileProcessor.make_patients(self.root_path)
        print ConfigProcessor(self.config_path, patients).render_template()
