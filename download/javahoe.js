window.onload = function(){
	var x = 1;
	const img1 = document.getElementById("dl");
	const lel = document.getElementById("soeinscheiß");
	function hehe() {
		if (x == 1) {
			img1["src"] = "images/Download2.png";
			x=2;
		} else if (x == 2){
			img1["src"] = "images/Download.png";
			x=1;
		}
		lel.appendChild(img1);
	}
	
}



		
