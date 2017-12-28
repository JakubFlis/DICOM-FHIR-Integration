# DICOM integration with FHIR HL7 based backend server - Server module
> A group project from Gdansk University of Technology

### Installation
The `Integration` module should work with any FHIR compliant backend server. For purposes of the development, the   [HAPI-FHIR](https://github.com/jamesagnew/hapi-fhir) server has been used.

## HAPI-FHIR quick installation guide
1. Make sure you're using Java 1.8 and have Maven installed and configured properly,
2. Download the [HAPI-FHIR](https://github.com/jamesagnew/hapi-fhir) server,
3. Run in terminal from the main hapi-fhir's directory:

```sh
$ mvn install -DskipTests
```

4. After the build process has finished, navigate to `/hapi-fhir-jpaserver-example` folder:

```sh
$ cd hapi-fhir-jpaserver-example/
```

5. Run the `jetty` server with following command:

```sh
$ mvn jetty:run
```

6. After a while, a running FHIR server should be available under `localhost:8080/hapi-fhir-jpaserver-example/`.

More HAPI-FHIR installation guides:
[Here](http://hapifhir.io/doc_jpa.html) and [here](https://www.openhealthhub.org/t/howto-build-a-health-database-and-fhir-api-server-in-15-mins-using-open-source/155).