// This example creates a simple polygon representing the Bermuda Triangle.
function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 5,
    center: { lat: 39.9296662, lng: -96.1336568 },
  });
  // Define the LatLng coordinates for the polygon's path.

  var AWS = "#fb8500";
  var Azure = "#219ebc";
  var GCP = "#ffb703";

  colors = [AWS, Azure, GCP]

  function jobs(val1) {
    highlight = colors[Math.floor(Math.random()*colors.length)];
    const val = new google.maps.Polygon({
      paths: val1,
      strokeColor: highlight,
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: highlight,
      fillOpacity: 0.35,
    });
    val.setMap(map);
  }

  states.forEach(element => {jobs(element)});

}
