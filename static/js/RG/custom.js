$(document).ready(function(){
	$(".btnBlue").click(function(){
		$("#layerAlram").show();
		return false;
	});
	$(".layerClose, .shadow").click(function(){
		$("#layerAlram").hide();
		return false;
	});

});