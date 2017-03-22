$(document).ready(function() {
	$.ajax({
		url: "52.33.88.132:5000/historical/20130101"
	}).then(function(data){
		$(".forecast-info").append(data.content);
	});
});
