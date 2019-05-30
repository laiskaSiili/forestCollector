var map = L.map('map').setView([0,0], 5);
L.tileLayer(
  'http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
  }).addTo(map);

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

var markers = [];
for (var i=0; i<points.length; i++) {
  var marker = L.marker(points[i]);
  marker.bindPopup(pointsPopup[i]);
  marker.addTo(this.map);
  markers.push(marker);
}

