# DICOM integration with Kainos Evolve Velocity platform - Integration module
> A group project from Gdansk University of Technology

### Installation
This application requires [Python 2.7.*](https://www.python.org/download/releases/2.7/) to run.

Dependencies:
- [PyDicom](http://www.pydicom.org/)
- [Jinja2](http://jinja.pocoo.org/docs/2.9/)

Dependencies can be installed via `pip` command, for example:

```sh
$ pip install pydicom
$ pip install jinja
```

Instead of using `pip`, it is also possible to use `easy_install` for installing dependencies:

```sh
$ easy_install pydicom
$ easy_install jinja
```

### Usage

The DICOM processor requires a path to the root folder, which should contain other folders and files grouped as follows:
```sh
|- Root 
   |- Patients
      |- Studies
         |- Series
            |- Instances (.dcm files)
```

Following flags must be provided:
- For specifying the root path:
```sh
-i <root_path>
```
- For specifying the template (configuration file) path:
```sh
-c <template_path>
```
- For specifying the output file path:
```sh
-o <output_file_path>
```

All three flags are mandatory.

Example:

```sh
$ python main.py -i ./DicomRootFolder -c ./template.jinja -o output.txt
```

### Templating

The Integration engine uses Jinja2 templating system to map DICOM objects into output files. [Jinja2 documentation](http://jinja.pocoo.org/docs/2.9/)

Most common templating expressions:
- `{% for x in y %}` - a for loop enumerating through `y` variable. Must end with `{% endfor %}` expression.
- `{{ x }}` - prinitng the `x` variable value to the output file. `{{ x.y() }}` will call `y()` function that is accessible from object `x`.

While creating a template, following properties are available for the user: 
- `patients` (an array of Patient objects), `studies` (stored in every `patients` array element), `series` (stored in every `studies` array element) and `instances` (stored in every `series` array element). 
- `patients`, `study` and `series` objects have a property called `random_dicom`, which allows the user to access any object from given set of objects. 
- `instance` objects have a function called `read_property` that reads the DICOM file's tag under given coordinates. 

Example use case:

Let's say the user wants to print all IDs from all `Series` in the root directory.
Series ID is stored inside the DICOM file under 0x20, 0x0E tag. 
Sample template that would print all IDs in new line would be as follows:

```sh
{% for patient in patients %}
    {% for studies in patient.studies %}
        {% for series in studies.series %}
            ID: {{ series.random_dicom.read_property("0x20", "0x0E") }}
        {% endfor %}
    {% endfor %}
{% endfor %}
```
