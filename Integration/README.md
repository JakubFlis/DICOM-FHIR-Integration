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