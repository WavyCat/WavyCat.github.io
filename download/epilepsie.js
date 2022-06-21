window.onload = function(){
	var x = 5;
	const coun = document.getElementById("brrr");
	function counter() {
		if (x != -1) {
			coun.innerHTML = x +"...";
			x-=1;
		} else if (x == -1){
			coun.innerHTML = "";
			location.href="file:///C:/Users/maxku/Desktop/bruh/index.html";
		}
	}
	window.setInterval(counter,1000);
}