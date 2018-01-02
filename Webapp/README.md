# DICOM integration with FHIR HL7 based backend server - Webapp module
> A group project from Gdansk University of Technology

### Web Application
Frotend site of the project is based on [AdminLTE](https://github.com/almasaeed2010/AdminLTE) template project.

### Installation
The AdminLTE template does not require any third party dependencies to run. It uses static HTML files JavaScript functios to connect with FHIR backed server and display sample results. 

File `imagingStudyWidgets.js` containt JavaScript functions for maintaining and controlling the ImagingStudy widgets. `imagingStudyUrl` variable should be changed to proper URL value before running the web application.

`WARNING`
If running the `hapi-fhir` server locally, CORS (example plugin [here](https://chrome.google.com/webstore/detail/allow-control-allow-origi/nlfbmbojpeacfghkpbjhddihlkkiljbi) policy may have to be disabled in local browser (for example, the Chrome browser does not have the CORS policy disabled by default).