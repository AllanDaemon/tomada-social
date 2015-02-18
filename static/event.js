var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    osmAttrib = '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  osm = L.tileLayer(osmUrl, {maxZoom: 19, minZoom: 3, attribution: osmAttrib});

var map = L.map('map',{
        contextmenu: true,
        contextmenuWidth: 140,
        contextmenuItems: [{
            text: 'Setar ponto aqui',
            callback: addMarker
        }, {
            text: 'Centralizar aqui',
            callback: centerMap
        }, '-', {
            text: 'Mais zoom',
            icon: '/static/images/zoom-in.png',
            callback: zoomIn
        }, {
            text: 'Menos zoom',
            icon: '/static/images/zoom-out.png',
            callback: zoomOut
        }]     
    })
    .addLayer(osm)
    .locate({setView: true, zoom: 16});

map.on('locationfound', function(e){
    if(marker==null){
        addMarker(e.latlng);
    }
});

map.on('locationerror', function(e){
    if(marker==null){
        map.setView(latlngDefault);
        addMarker(latlngDefault);
    }
});

latlngDefault = {lat:-15.28,lng:-52.20};
marker = null;

function addMarker(latlng){
    if (marker !== null) {
        map.removeLayer(marker);
    }

    if (latlng.latlng != null) {
        latlng = latlng.latlng;
    }
    
    marker = new L.marker(latlng, {draggable:'true'});
    map.addLayer(marker);
    updateLocationField(latlng);
    marker.on('dragend', function(e){
        latlng = marker.getLatLng();
        marker.setLatLng(latlng);
        updateLocationField(latlng);
    });
}

function updateLocationField(latlng){
    $('#lat').val(latlng.lat);
    $('#lng').val(latlng.lng);   
}

function centerMap (e) {
    map.panTo(e.latlng);
}

function zoomIn (e) {
    map.zoomIn();
}

function zoomOut (e) {
    map.zoomOut();
}

$('#date_start, #date_end').datetimepicker({
    locale: 'pt-BR'
});
$("#date_start").on("dp.change",function (e) {
    $('#date_end').data("DateTimePicker").minDate(e.date);
});
$("#date_end").on("dp.change",function (e) {
    $('#date_start').data("DateTimePicker").maxDate(e.date);
});
