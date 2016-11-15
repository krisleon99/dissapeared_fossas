 <script type="text/javascript">
    var marker = null;

  	console.log("mapa");

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

    //marker = L.marker([19.353600, -99.165689], {draggable:true})
    //marker.bindPopup("<div onClick='sendPoints()'><img class='btn-point' title='Agregar la ubicación' src='{{STATIC_URL}}base/img/add_point.svg'/></div>").addTo(map);;
          
    //marker.bindPopup("<div data-toggle='modal' data-target='#development'><img class='btn-point' title='Agregar la ubicación' src='{{STATIC_URL}}base/img/add-documents.svg'/></div>").addTo(map);

    // create the geocoding control and add it to the map
    var searchControl = L.esri.Geocoding.geosearch().addTo(map);

    // create an empty layer group to store the results and add it to the map
    var results = L.layerGroup().addTo(map);

  // listen for the results event and add every result to the map
    searchControl.on("results", function(data) {
        results.clearLayers();
        for (var i = data.results.length - 1; i >= 0; i--) {
        	marker = new L.marker(data.results[i].latlng, {draggable:true});
        	marker.bindPopup("<div onClick='sendPoints()'><img class='btn-point' title='Agregar la ubicación' src='{{STATIC_URL}}base/img/add_point.svg'/></div>");
          //marker.bindPopup("<div data-toggle='modal' data-target='#development'><img class='btn-point' title='Agregar la ubicación' src='{{STATIC_URL}}base/img/add-add_point.svg'/></div>");

          results.addLayer(marker);
        } 
    });


  function sendPoints() {
       console.log(marker);
       $.ajax({
         data: {'points': JSON.stringify([marker._latlng.lat,marker._latlng.lng]),
                csrfmiddlewaretoken: '{{ csrf_token }}'
               },
         url: '/fossas/address/update_point_fosas/',
         type: 'POST',
         success : function(data) {
                      console.log("a wevo");
                      console.log(data);
                      alert("ubicación actualizada");
                      console.log("wiuu");
         },
         error : function(message) {
                 console.log(message);
              }
       });
	}

</script>