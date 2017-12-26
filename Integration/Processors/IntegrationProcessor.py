""" IntegrationProcessor module """
import datetime
import json
from Processors.FileProcessor import FileProcessor
from Processors.ConfigProcessor import ConfigProcessor
from RequestHandler import RequestHandler

class IntegrationProcessor(object):
    """ This class manages other processors into one integration pipeline. """

    def __init__(self, config_path, root_path, output_path):
        self.config_path = config_path
        self.root_path = root_path
        self.output_path = output_path
        self.request_handler = RequestHandler()

    def integrate(self):
        """ Main integrating function. Binds FileProcessor and ConfigProcessor together.
        First, an array of patients is being made based on what is inside the folder under the given path.
        Then, the ConfigProcessor parses the template from the given path and renders the output. """
        print "\033[95mStarted Integration Engine on " + unicode(datetime.datetime.now()) + "\033[0m"
        # Creating the patient array
        print "Processing the root folder structure ..."
        patients = FileProcessor().make_patients(self.root_path)
        # Generating result based on the config file
        print "Reading the template file..."
        result = ConfigProcessor(self.config_path, patients).render_template()
        # Writing the result to the output file
        print "Saving the output file..."
        self.save_to_file(result)
        # Sending a request to FHIR backend (if applicable)
        if self.request_handler.should_send_requests == "true":
            print "Making a " + self.request_handler.method + " request to " + self.request_handler.url
            self.send_final_request()
        else:
            print "Making requests is turned off."

        print "\033[92mFinished.\033[0m"

    def save_to_file(self, string):
        """ Saves given string to a file. """
        with open(self.output_path, "w") as text_file:
            text_file.write(string)
            print "Saved to file " + self.output_path

    def send_final_request(self):
        """ Sends a request to FHIR backend """
        with open(self.output_path, "r") as text_file:
            data = json.load(text_file)
            print self.request_handler.send(data)