document.addEventListener('DOMContentLoader',function(){

	alert("page is loaded")
    var start = 0,end =0;
	var best = 10000, sum=0, i=0, timeTaken=0,j=0;
	start = new Date().getTime();
	
	
	function getRandomColor() {
		var letters = '0123456789ABCDEF';
		var color = '#';
		for (var i = 0; i < 6; i++) {
					color += letters[Math.floor(Math.random() * 16)];
							}
		return color;
	  }
	
	
      function delay(){
        setTimeout(makeShapeAppear,Math.random()*2000 ) ;
        
    }
    function makeShapeAppear(){
        document.getElementById("playarea").style.width = "90%" ;
        start = new Date().getTime();
    }
	
	function update(){
		document.getElementById("ls").innerHTML = "Last Score : : " + timeTaken + " sec.";
		document.getElementById("bs").innerHTML = "Best Score : " + best + " sec.";   
		document.getElementById("as").innerHTML = "Avg. Score : " + sum/i + " sec.";
	}
	
	
	document.getElementById("start").onclick = function(){
		j++ ;            
		document.getElementById("start").style.display ="none" ;
		document.getElementById("playarea").style.backgroundColor = getRandomColor() ;
        document.getElementById("playarea").style.width = "0%" ; 
        delay();
		}
	
	document.getElementById("playarea").onclick = function(){
			if(i>=6){
				alert("Well done, Round finished!");
                update();
                document.getElementById("playarea").style.width = "0%" ;
				i = 0;j=0 ;
                document.getElementById("start").style.display ="block" ;
                document.getElementById("start").innerText = "Play Again"
			}
			else if(j > 0){
				end = new Date().getTime();
				timeTaken = (end - start)/1000;
                alert( timeTaken + "sec.")
				document.getElementById("playarea").style.width = "0%" ; 
				if ( timeTaken < best ){
					best = timeTaken ;
				}
				sum = sum + timeTaken ;
				i++ ;
                document.getElementById("playarea").style.backgroundColor = getRandomColor() ;
                delay(); 
			}
			else{
				alert("click on start button to play");
			}
		}
});