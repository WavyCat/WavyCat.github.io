window.onload = function(){
	var x = 5;
	const coun = document.getElementById("brrr");
	function counter() {
		if (x != -1) {
			coun.innerHTML = x +"...";
			x-=1;
		} else if (x == -1){
			coun.innerHTML = "";
			location.href="wavycat.github.io/download/index.html";
		}
	}
	window.setInterval(counter,1000);
}
