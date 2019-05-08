'use strict';

class Map {
  constructor(conf) {
    this.mapContainerId = conf['mapContainerId'];
    this.errorEl = document.getElementById(conf['errorElId']);
    this.initialPosition = conf['initialPosition'];
    this.initialZoom = conf['initialZoom'];
    this.map = map = L.map(this.mapContainerId).setView(this.initialPosition, this.initialZoom);
    // Set up the Google Satellite layer
    L.tileLayer(
      'http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
        maxZoom: 20,
        subdomains:['mt0','mt1','mt2','mt3']
      }).addTo(this.map);
    // add a marker in the given location
    this.marker  = L.marker(this.initialPosition);
    this.marker.addTo(this.map);
    // Initialize geolocation
    if (navigator.geolocation) {
      this.geolocator = navigator.geolocation;
    } else {
      this.errorEl.textContent = "Geolocation is not supported!";
    }
  }

  flyTo(latLng, zoom) {
    this.map.flyTo(latLng, zoom);
  }

  moveMarker(latLng) {
    this.marker.setLatLng(latLng);
  }

  getLocation(callback) {
    this.geolocator.getCurrentPosition(function(position) {
      callback(position);
    }, this._showError.bind(this));
  }

  _showError(error) {
    switch(error.code) {
      case error.PERMISSION_DENIED:
        this.errorEl.textContent = "User denied the request for Geolocation."
        break;
      case error.POSITION_UNAVAILABLE:
        this.errorEl.textContent = "Location information is unavailable."
        break;
      case error.TIMEOUT:
        this.errorEl.textContent = "The request to get user location timed out."
        break;
      case error.UNKNOWN_ERROR:
        this.errorEl.textContent = "An unknown error occurred."
        break;
    }
  }
}

/* --------------------
  ENTRY POINT
---------------------*/

// instantiate map object
var mapConf = {
  'mapContainerId': 'map',
  'errorElId': 'getLocationBtn',
  'initialPosition': [37.46367, 6.46326],
  'initialZoom': 6
}
var mapObj = new Map(mapConf);

// get important dom elements
var latInput = document.getElementById('id_lat');
var lonInput = document.getElementById('id_lon');
var accuracyInput = document.getElementById('id_accuracy');
var getLocationBtn = document.getElementById('getLocationBtn');

// Listen to click events on geolocationbtn to get current location.
getLocationBtn.addEventListener('click', function(event) {
  event.stopPropagation();
  mapObj.getLocation(setPositionToInputs);
});
// Listen to click events on map to set clicked location
mapObj.map.on('click', onMapClick);

function writePositionDataToInputs(latLngAcc) {
  latInput.value = latLngAcc.lat.toFixed(5);
  lonInput.value = latLngAcc.lng.toFixed(5);
  if (latLngAcc.accuracy) {
    accuracyInput.value = latLngAcc.accuracy.toFixed(3);
  }
}

function setPositionToInputs(position) {
  let latLngAcc = {
    lat:position.coords.latitude, 
    lng:position.coords.longitude,
    accuracy: position.coords.accuracy
  }
  writePositionDataToInputs(latLngAcc);
  mapObj.flyTo(latLngAcc, 18);
  mapObj.moveMarker(latLngAcc);
}

function onMapClick(event) {
  let latLngAcc = event.latlng;
  latLngAcc['accuracy'] = null;
  writePositionDataToInputs(latLngAcc);
  mapObj.moveMarker(latLngAcc);
}


