// !!! CHANGE THIS URL TO PROPER SERVER URL VALUE !!! // 
var imagingStudyUrl = "http://api.fhir.eti:8080/hapi-fhir-jpaserver-example/baseDstu3/ImagingStudy?_pretty=true";
var diagnosticReportUrl = "http://api.fhir.eti:8080/hapi-fhir-jpaserver-example/baseDstu3/DiagnosticReport?_pretty=true";

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

// -- All Series counter Widget -- //
function refreshAllSeriesCounterWidget(data) {
    var parsedJson = JSON.parse(data);
    var seriesInTotal = 0;
    var instancesInTotal = 0;

    if (parsedJson.entry != undefined) {
        parsedJson.entry.forEach(element => {
            seriesInTotal += element.resource.series.length;
            element.resource.series.forEach(series => {
                instancesInTotal += series.instance.length;
            });
        });
    }

    // Series
    jQuery("#total-series-objects").html(seriesInTotal);
    jQuery("#total-series-objects-loading").hide();

    // Instances
    jQuery("#total-instances-objects").html(instancesInTotal);
    jQuery("#total-instances-objects-loading").hide();
}

// -- ImagingStudy list widget -- //
function prepareInstancesHTML(series) {
    var instanceHtml = "";
    if (series.instance != undefined && series.instance.length > 0) {
        instanceHtml += " (Total: " + series.instance.length + ")" + "<ol>";
        series.instance.forEach(instance => {
            instanceHtml += "<li><img src=\"icon_instance.png\"/> " + instance.sopClass + " no. " + instance.number + "</li>";
        });
        instanceHtml += "</ol>";
    }

    return instanceHtml;
}

function prepareSeriesHTML(allSeries) {
    var seriesHtml = "<ul>";
    allSeries.forEach(series => {
        seriesHtml += "<li><img src=\"icon_series.png\"/> " + series.description;
        seriesHtml += prepareInstancesHTML(series);
        seriesHtml += "</li>";
    });
    seriesHtml += "</ul>";

    return seriesHtml;
}

function refreshImagingStudyListWidget(data) {
    // Downloading all ImagingStudy objects form backend
    var parsedJson = JSON.parse(data);
    var startSection = "<div class=\"panel-group\" id=\"accordion\">";
    var endSection = "</div>";
    var contentSection = "";

    if (parsedJson.entry != undefined) {
        parsedJson.entry.forEach(element => {
            var id = element.resource.id;
            var description = element.resource.description == undefined ? element.resource.series[0].description : element.resource.description;
            description = description.replace('^', ' ');
            var lastUpdated = new Date(element.resource.meta.lastUpdated).toDateString();
            var numberOfSeries = element.resource.series.length;
            var seriesList = prepareSeriesHTML(element.resource.series);
    
            contentSection += "<div class=\"panel panel-default\"><div class=\"panel-heading\"><h4 class=\"panel-title\"><a data-toggle=\"collapse\" data-parent=\"#accordion\" href=\"#" + id + "\"><img src=\"icon_imagingstudy.png\"/> " + description + "</a><span class=\"pull-right badge bg-blue\">" + numberOfSeries + " series</span></h4></div><div id=\"" + id + "\" class=\"panel-collapse collapse\"><div class=\"panel-body\"><!-- content start -->ID: <i>" + id + "</i><br/>Last updated: <i>" + lastUpdated + "</i><br/><u>Series:</u><br/>" + seriesList + "<!-- content end --></div></div></div>";
        });
        jQuery("#imagingstudy-box").html(startSection + contentSection + endSection);
    } else {
        jQuery("#imagingstudy-box").html("<p style=\"color: gray; font-size: 12pt;\">No entries</p>");
    }

    jQuery("#imagingstudy-box-loading").hide();
}

function refreshDiagnosticReportListWidget(data) {
    // Downloading all DiagnosticReport objects form backend
    var parsedJson = JSON.parse(data);
    var startSection = "<div class=\"panel-group\" id=\"accordion\">";
    var endSection = "</div>";
    var contentSection = "";

    if (parsedJson.entry != undefined) {
        parsedJson.entry.forEach(element => {
            var id = element.resource.id;
            var description = element.resource.subject.display.split('^').join(' ');
            var lastUpdated = new Date(element.resource.meta.lastUpdated).toDateString();
            var conclusion = element.resource.conclusion;
            var status = element.resource.text.status.toUpperCase();

            contentSection += "<div class=\"panel panel-default\"><div class=\"panel-heading\"><h4 class=\"panel-title\"><a data-toggle=\"collapse\" data-parent=\"#accordion\" href=\"#" + id + "\">" + description + "</a><span class=\"pull-right badge bg-red\">STATUS: " + status + "</span></h4></div><div id=\"" + id + "\" class=\"panel-collapse collapse\"><div class=\"panel-body\"><!-- content start --><br/>Last updated: <i>" + lastUpdated + "</i><br/><div>" + conclusion + "</div><!-- content end --></div></div></div>";
        });
        jQuery("#diagnosticreport-box").html(startSection + contentSection + endSection);
    } else {
        jQuery("#diagnosticreport-box").html("<p style=\"color: gray; font-size: 12pt;\">No entries</p>");
    }
    
    jQuery("#diagnosticreport-box-loading").hide();
}

httpGetAsync(imagingStudyUrl, function(data) {
    refreshAllImagingStudiesCounterWidget(data);
    refreshAllSeriesCounterWidget(data);
    refreshImagingStudyListWidget(data);
});

httpGetAsync(diagnosticReportUrl, function(data) {
    refreshDiagnosticReportListWidget(data);
});