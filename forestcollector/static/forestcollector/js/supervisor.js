// initialize leaflet map
var map = L.map('map').setView([0,0], 5);
L.tileLayer(
    'http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
}).addTo(map);

// extract lat, lon and popup text from html table into arrays
var latlngHtml = document.getElementsByClassName('latlng');
var points = [];
var pointsPopup =[];
for (var i=0; i<latlngHtml.length; i++) {
    var lat = Number(latlngHtml[i].dataset.lat);
    var lon = Number(latlngHtml[i].dataset.lon);
    var popup =String(latlngHtml[i].dataset.popup);
    points.push([lat, lon]);
    pointsPopup.push(popup);
}

// create markers from points list
var markers = {};
for (var i=0; i<points.length; i++) {
    var marker = L.marker(points[i]);
    var rowId = latlngHtml[i].id;
    marker.bindPopup(pointsPopup[i]);
    marker.rowId = rowId;
    marker.addTo(this.map);
    markers[rowId] = marker;
}

// Zoom map to bounding box of all markers. Add a little padding to display markers more in center.
var group = new L.featureGroup(Object.values(markers));
map.fitBounds(group.getBounds().pad(0.5));

/* -------------
    EVENT LISTENERS
 ------------- */

// on table row click, highlight row and open marker popup
Array.from(document.getElementsByTagName('tr')).forEach(function(row) {
    row.addEventListener('click', highlightOnRowClick)
});

// on marker click, highlight corresponding row
for (var rowId in markers) {
    markers[rowId].addEventListener('click', highlightOnMarkerClick)
}

// if only map is clicked, remove all highlights from rows
map.on('click', removeAllHighlights);

/* -------------
    FUNCTIONS
 ------------- */

function removeAllHighlights() {
    // for each table row, remove class highlight
    Array.from(document.getElementsByTagName('tr')).forEach(function(row) {
        row.classList.remove('highlight');
    });
}

// highlight row with specified id.
function highlightRow(rowId) {
    removeAllHighlights();
    var rowToHighlight = document.getElementById(rowId);
    if (rowToHighlight) {
        rowToHighlight.classList.add('highlight');
    }
}

function highlightOnMarkerClick(event) {
    // get rowId attribute from clicked marker, which corresponds to the table row id.
    var rowId = event.target.rowId;
    // add class highlight to row with id corresponding to clicked marker
    highlightRow(rowId);
}

function highlightOnRowClick(event) {
    var rowId = event.currentTarget.id;
    // highlight clicked row
    highlightRow(rowId);
    // close all map popups
    map.closePopup();
    // open popup of clicked row
    markers[rowId].openPopup();
}