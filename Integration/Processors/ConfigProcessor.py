import jinja2

class ConfigProcessor(object):
    def __init__(self, template_file_path, patients): 
        templateLoader = jinja2.FileSystemLoader( searchpath="./Processors/" )
        templateEnv = jinja2.Environment(loader=templateLoader, trim_blocks=True, lstrip_blocks=True)
        self.template = templateEnv.get_template("template.jinja")
        self.template_vars = {"studies": patients[0].studies}

    def render_template(self):
        return self.template.render(self.template_vars)
