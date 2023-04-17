window.onload = function(){
	var x = 1;
	const box = document.getElementById("aaa");
	function hehe() {
		if (x == 1) {
			box.style.background = "#009FB7";
			x=2;
		} else if (x == 2){
			box.style.background = "#FED766";
			x=1;
		}
	}
	window.setInterval(hehe,100);
}
