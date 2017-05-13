# DICOM integration with Kainos Evolve Velocity platform
> A group project from Gdansk University of Technology

### Installation
This application requires [Python 2.7.*](https://www.python.org/download/releases/2.7/) to run.

Dependencies:
- [PyDicom](http://www.pydicom.org/)

Dependencies can be installed via `pip` command, for example:

```sh
$ pip install pydicom
```

### Usage

An empty file path with .dcm extension (DICOM file) must be provided using i- <inputfile> flag, for example:

```sh
$ main.py -i SampleDICOM/USG.dcm
```