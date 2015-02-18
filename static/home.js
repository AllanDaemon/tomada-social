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
radius = 42;

function addMarker(latlng){
    if (marker !== null) {
        map.removeLayer(marker);
    }

    if (latlng.latlng != null) {
        latlng = latlng.latlng;
    }

    var RedIcon = L.Icon.Default.extend({
        options: {
            iconUrl: '/static/images/marker-icon-red.png' 
        }
     });
     var redIcon = new RedIcon();

    marker = new L.marker(latlng, {
        draggable:'true',
        icon: new RedIcon()});
    map.addLayer(marker);
    getEvent();
    marker.on('dragend', function(e){
        latlng = marker.getLatLng();
        marker.setLatLng(latlng);
        getEvent();
    });
    
    map.addLayer(marker);
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



var listMarkers = new Array();

function clearMarkers(){
    for(i=0; i<listMarkers.length; i++){
        map.removeLayer(listMarkers[i]);
    }
    listMarkers = new Array()
}


var maskDate = function(date){
    return ("0"+date.getDate()).slice(-2) + '/' + ("0"+(date.getMonth() + 1)).slice(-2) + '/' + date.getYear().toString().slice(-2); 
}

var dateIni,
    nav,
    dateCur = new Date().getTime()

dateNav(dateCur)

function dateNav(dateIni){
    dateIni = new Date(dateIni-86400000*2).getTime();

    $nav = $('#nav').empty()
    for(inc=0; inc<6; inc++){
        date = new Date(dateIni+86400000*inc);
        dateM = maskDate(date);
        dt = date.getTime();
        $bt = $('<button class="btnDate btn btn-default '+((dateCur==dt)?'active':'')+' navbar-btn col-lg-2 col-md-2 col-xs-2 col-sm-2" data-date="'+dt+'">'+dateM+'</button>');
        $nav.append($bt);
    }
}

$('body').on('click','.btnDate', function(){
    dt = $(this).attr('data-date');
    dateCur = dt;
    dateNav(dt);
    getEvent();
});

function getEvent(){
    data = {
        radius: radius,
        lat: marker.getLatLng().lat,
        lng: marker.getLatLng().lng,
        date:dateCur
    }
    var events = $.ajax({
        type: 'GET',
        data: data,
        url: '/event/search/',
        dataType: 'json',
        success: function(json) {
            clearMarkers()
            if(typeof json != 'undefined'){
                for (var i = 0; i < json.length; i++) {
                    if(json[i].location != null){
                        var markerSearch = L.marker(json[i].location);
                        listMarkers.push(markerSearch);
                        markerSearch.addTo(map);
                        markerSearch.bindPopup(
                            "<div class='bindPopup'>"+
                            "<p class='title'>"+ json[i].title+"</p>"+
                            "<p class='date'><b>Data Inicial</b>:"+ json[i].date_start+"</p>"+
                            ((json[i].date_end!='')?"<p class='date'><b>Data Final</b>:"+ json[i].date_end+"</p>":'')+
                            "<p class='more'><a href='/event/"+ json[i].id+"/detail'>Ver mais</a></p>"+
                            "</div>");
                    }
                }

            }
        }
    });    
}