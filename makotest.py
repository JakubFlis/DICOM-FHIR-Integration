import jinja2
import random
import time
import string

class Folder: 
    def getAnyDicom(self):
        raise NotImplementedError

class Study(Folder):
    path = None

    def __init__(self):
        self.series = [Series() for count in xrange(2)]

    def getAnyDicom(self):
        return random.choice(self.series).getAnyDicom()
    
class Series(Folder):
    path = None

    def __init__(self):
        self.instances = [Instance() for count in xrange(3)]
        self.path = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
        for instance in self.instances:
            instance.seriesPath = self.path 

    def getAnyDicom(self):
        return random.choice(self.instances)

class Instance:
    seriesPath = None

    def __init__(self):
        self.pathToFile = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

    def readProperty(self, coords):
        return "A property from coords: " + coords + " of path " + str(self.pathToFile)



templateLoader = jinja2.FileSystemLoader( searchpath="./" )
templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True, lstrip_blocks=True)
TEMPLATE_FILE = "template.jinja"
template = templateEnv.get_template(TEMPLATE_FILE)

# Here we add a new input variable containing a list.
# Its contents will be expanded in the HTML as a unordered list.
FAVORITES = [ "chocolates", "lunar eclipses", "rabbits" ]

STUDIES = [Study() for count in xrange(1)] # This will be a result of folder scanning

def getAny(string):
   return "This is any DICOM file " + string

def nestedFunction(string):
    return string + " is nested."


templateVars = { "studies": STUDIES }

print(template.render(templateVars))