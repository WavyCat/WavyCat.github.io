document.addEventListener('keydown', function(event) {
    if (event.keyCode == 187) { //Plus
        document.getElementById("team1").innerHTML = (parseInt(document.getElementById("team1").innerHTML) + 1);

    }
    else if (event.keyCode == 189) { //Minus
        document.getElementById("team1").innerHTML = (parseInt(document.getElementById("team1").innerHTML) - 1);
    }
    else if (event.keyCode == 38) { //Hoch
        document.getElementById("team2").innerHTML = (parseInt(document.getElementById("team2").innerHTML) + 1);
    }
    else if (event.keyCode == 40) { //Runter
        document.getElementById("team2").innerHTML = (parseInt(document.getElementById("team2").innerHTML) - 1);
    }
}, true);
