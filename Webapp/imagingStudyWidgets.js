
var imagingStudyUrl = "http://api.fhir.eti:8080/hapi-fhir-jpaserver-example/baseDstu3/ImagingStudy?_pretty=true";

function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true);
    xmlHttp.send(null);
}

// -- All ImagingStudies counter Widget -- //
function refreshAllImagingStudiesCounterWidget(data) {
    var parsedJson = JSON.parse(data);
    jQuery("#total-imagingstudy-objects").html(parsedJson.total);
    jQuery("#total-imagingstudy-objects-loading").hide();
}

// -- ImagingStudy list widget -- //
function prepareInstancesHTML(series) {
    var instanceHtml = "";
    if (series.instance != undefined && series.instance.length > 0) {
        instanceHtml += " (" + series.instance.length + ")" + "<ul>";
        series.instance.forEach(instance => {
            instanceHtml += "<li>" + instance.sopClass + "</li>";
        });
        instanceHtml += "</ul>";
    }

    return instanceHtml;
}

function prepareSeriesHTML(allSeries) {
    var seriesHtml = "<ul>";
    allSeries.forEach(series => {
        seriesHtml += "<li>" + series.description;
        seriesHtml += prepareInstancesHTML(series);
        seriesHtml += "</li>";
    });
    seriesHtml += "</ul>";

    return seriesHtml;
}

function refreshImagingStudyListWidget(data) {
    // Downloading all ImagingStudies form backend
    var parsedJson = JSON.parse(data);
    var startSection = "<div class=\"panel-group\" id=\"accordion\">";
    var endSection = "</div>";
    var contentSection = "";

    parsedJson.entry.forEach(element => {
        var id = element.resource.id;
        var description = element.resource.description;
        var lastUpdated = element.resource.meta.lastUpdated;
        var numberOfSeries = element.resource.series.length;
        var seriesList = prepareSeriesHTML(element.resource.series);

        contentSection += "<div class=\"panel panel-default\"><div class=\"panel-heading\"><h4 class=\"panel-title\"><a data-toggle=\"collapse\" data-parent=\"#accordion\" href=\"#" + id + "\">" + description + "</a></h4></div><div id=\"" + id + "\" class=\"panel-collapse collapse\"><div class=\"panel-body\"><!-- content start -->ID: <i>" + id + "</i><br/>Last updated: <i>" + lastUpdated + "</i><br/><u>Series:</u><br/>" + seriesList + "<!-- content end --></div></div></div>";
    });

    jQuery("#imagingstudy-box").html(startSection + contentSection + endSection);
    jQuery("#imagingstudy-box-loading").hide();
}

httpGetAsync(imagingStudyUrl, function(data) {
    refreshAllImagingStudiesCounterWidget(data);
    refreshImagingStudyListWidget(data);
});
