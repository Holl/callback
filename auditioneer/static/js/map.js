/**
 * Created by Holl on 3/17/14.
 */

function initizalize() {

	//This function brings up the map.
	//Defualt is set to 0,0, min zoom.

    mapOptionsObject = {
        center: new google.maps.LatLng(0, 0),
        zoom: 1,
        mapTypeId: google.maps.ROADMAP,



    };

    MapOnThePage = new google.maps.Map(
    document.getElementById('map-canvas'),
    mapOptionsObject);

    console.log("Map has initzalized.");

}


google.maps.event.addDomListener(window, 'load', initizalize);


$(document).ready(function () {
    $("#id_location_name").keypress(function() {

            setTimeout(function() {dropPoint($('#id_location_name').val())}, 1250);

    });
})

function dropPoint(zone){

    var userCity = zone;
    geocoderData = new google.maps.Geocoder();

    geocoderData.geocode({
        'address': userCity
    }, function (results) {


        city=results;
        MapOnThePage.setCenter(results[0].geometry.location);

        MapOnThePage.setZoom(14);

        console.log(results[0].geometry.location)

        $("#id_latitude").val(results[0].geometry.location.k)
        $("#id_longitude").val(results[0].geometry.location.A)


    });
}