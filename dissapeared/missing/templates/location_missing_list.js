 <script type="text/javascript">
    var marker = null;

  	var baseLayer1 = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
  	var baseLayer2 = new L.TileLayer('http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png');
  	var baseLayer3 = new L.TileLayer('http://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png');

  	var baseLayers = {
     "Streets": baseLayer1,
     "Gray": baseLayer2,
     "Purple": baseLayer3
     };


  	var sobreposiciones = new L.LayerGroup();
	
	var map = new L.Map('map', {
	  center: [24, -97],
    zoom: 5,
    maxZoom: 19,
    minZoom: 1,
	  layers: [baseLayer1]
	});

    L.control.layers(baseLayers).addTo(map);
          
    //marker.bindPopup("<div data-toggle='modal' data-target='#development'><img class='btn-point' title='Agregar la ubicación' src='{{STATIC_URL}}base/img/add-documents.svg'/></div>").addTo(map);

    // create the geocoding control and add it to the map
    var searchControl = L.esri.Geocoding.geosearch().addTo(map);

    // create an empty layer group to store the results and add it to the map
    var results = L.layerGroup().addTo(map);

  // listen for the results event and add every result to the map
    searchControl.on("results", function(data) {
        results.clearLayers();
        for (var i = data.results.length - 1; i >= 0; i--) {
        	var marker = new L.marker(data.results[i].latlng, {draggable:true});
        	marker.bindPopup("<div onClick='sendPoints()'><img class='btn-point' title='Agregar la ubicación' src='{{STATIC_URL}}base/img/add-documents.svg'/></div>");
          //marker.bindPopup("<div data-toggle='modal' data-target='#development'><img class='btn-point' title='Agregar la ubicación' src='{{STATIC_URL}}base/img/add-documents.svg'/></div>");

          results.addLayer(marker);
        } 
    });


  function sendPoints() {
       console.log(marker);
       var arr_po = [];
       arr_po.push(id_fossa);
       arr_po.push(marker._latlng.lat);
       arr_po.push(marker._latlng.lng);
       console.log("wiuuu");
       console.log(arr_po);
       $.ajax({
         data: {'points': JSON.stringify(arr_po),
                csrfmiddlewaretoken: '{{ csrf_token }}'
               },
         url: '/fossas/address/current_point_fosas/',
         type: 'POST',
         success : function(data) {
                      console.log("a wevo");
                      console.log(data);
         },
         error : function(message) {
                 console.log(message);
              }
       });
	}
$(document).ready(function(){
    console.log("que ok");
    console.log(arr_lat);
    for (var i = 0; i < arr_lat.length; i++) {
      l_t = arr_lat[i];
      l_n = arr_lng[i];
      console.log(l_t);
      console.log(l_n);
      marker = L.marker([l_n, l_t], {draggable:true})
      marker.bindPopup("<div onClick='sendPoints()'>ubicación<img class='btn-point' title='Actualizar ubicación' src='{{STATIC_URL}}base/img/see_map.svg'/></div>")
      marker.addTo(map);
    }
   
   
});
</script>