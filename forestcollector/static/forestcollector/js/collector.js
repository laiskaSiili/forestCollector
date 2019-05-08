// center of the map
var center = [37.46367, 18.46326];

// Create the map
var map = L.map('map').setView(center, 6);

// Set up the Google Satellite layer
L.tileLayer(
  'http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
  }).addTo(map);

// add a marker in the given location
var marker  = L.marker(center);
marker.addTo(map);


/* -------------------
  TRACKING
--------------------- */
var geolocator;
var tracking = false;
var trackingInterval;
var trackbtn = document.getElementById("trackBtn");
setupGeolocation();

if (!trackbtn.disabled) {
  trackbtn.addEventListener('click', switchTracking);
}

function setupGeolocation() {
  if (navigator.geolocation) {
    geolocator = navigator.geolocation;
  } else {
    trackBtn.textContent = "Geolocation is not supported!";
    trackBtn.disabled = true;
  }
}

function switchTracking() {
  if (tracking) {
    trackbtn.textContent = 'Start tracking';
    trackbtn.classList.remove('btn-warning');
    trackbtn.classList.add('btn-light');
    clearInterval(trackingInterval);
  } else {
    trackbtn.textContent = 'Tracking...';
    trackbtn.classList.add('btn-warning');
    trackbtn.classList.remove('btn-light');
    locate();
    trackingInterval = setInterval(locate, 5000);
  }
  tracking = !tracking;
}

function locate() {
  geolocator.getCurrentPosition(showPosition, showError);
}

function showPosition(position) {
  console.log(position);
  let latLng = {
    lat:position.coords.latitude, 
    lon:position.coords.longitude
  }
  marker.setLatLng(latLng);
  map.flyTo(latLng, 18);
}

function showError(error) {
  switch(error.code) {
    case error.PERMISSION_DENIED:
      trackbtn.innerHTML = "User denied the request for Geolocation."
      break;
    case error.POSITION_UNAVAILABLE:
      trackbtn.innerHTML = "Location information is unavailable."
      break;
    case error.TIMEOUT:
      trackbtn.innerHTML = "The request to get user location timed out."
      break;
    case error.UNKNOWN_ERROR:
      trackbtn.innerHTML = "An unknown error occurred."
      break;
  }
}
