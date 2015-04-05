(function(window, google){
	var options = {
		center:
		{
			lat:37,
			lng: -122
		},
		zoom: 10
		},
		element = document.getElementById("dvMap"),
		map = new google.maps.Map(element, options);
	
}(window, google));