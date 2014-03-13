/**
 * Created by Holl on 3/13/14.
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