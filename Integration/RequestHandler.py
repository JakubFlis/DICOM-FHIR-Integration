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
        print self.send("test").status_code

    def send(self, data):
        if self.method == "PUT":
            rsp = requests.post(self.url, json=data, headers=self.headers)
        elif self.method == "GET":
            rsp = requests.get(self.url, json=data, headers=self.headers)
        else:
            rsp = None
            print "Declare proper method (PUT or GET) in config JSON file."
        return rsp