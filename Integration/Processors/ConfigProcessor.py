""" ConfigProcessor template """
import jinja2
import os

class ConfigProcessor(object):
    def __init__(self, template_file_path, patients):
        path, file = os.path.split(template_file_path)
        template_loader = jinja2.FileSystemLoader(searchpath=path)
        template_environment = jinja2.Environment(loader=template_loader, trim_blocks=True, lstrip_blocks=True)
        self.template = template_environment.get_template(file)
        self.template_vars = {"studies": patients[0].studies}

    def render_template(self):
        """ Renders the output content based on given template. """
        return self.template.render(self.template_vars)
