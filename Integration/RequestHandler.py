import json
import requests

class RequestHandler(object):
    """ Class handling HTTP requests using config JSON file. """

    def __init__(self):
        with open('request_config.json') as data_file:
            self.data = json.load(data_file)
        self.url = self.data["URL"]
        self.method =  self.data["Method"]
        self.headers = self.data["Headers"]

    def send(self, data):
        if self.method == "POST":
            rsp = requests.post(self.url, json=data, headers=self.headers)
        elif self.method == "GET":
            rsp = requests.get(self.url, json=data, headers=self.headers)
        elif self.method == "PUT":
            rsp = requests.put(self.url, json=data, headers=self.headers)
        else:
            print "Declare proper method in config JSON file."
        return rsp.text