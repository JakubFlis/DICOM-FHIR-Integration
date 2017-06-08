import jinja2
from Models.Study import Study

class ConfigProcessor(object):
    def __init__(self, template_file_path, patients): 
        templateLoader = jinja2.FileSystemLoader( searchpath="./Processors/" )
        templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True, lstrip_blocks=True)
        TEMPLATE_FILE = "template.jinja" #template_file_path
        template = templateEnv.get_template(TEMPLATE_FILE)

        STUDIES = [Study() for count in xrange(1)] # This will be a result of folder scanning

        templateVars = { "studies": STUDIES }

        print template.render(templateVars)
