'use strict';

window.onload = function() {
	
	var canvas1 = document.getElementById("sketchbook1");
	
	if (canvas1 && canvas1.getContext) {
		var ctx = canvas1.getContext("2d");
		ctx.fillStyle = "#00C";
		ctx.fillRect(20, 20, 150, 80);
		ctx.strokeRect(0, 0, 90, 125);
		ctx.clearRect(25, 25, 35, 35);
		
		ctx.strokeStyle = "#030";	// 枠線の色
		ctx.lineWidth = 5;			// 枠線の太さ
		ctx.beginPath();
		ctx.moveTo(50, 100);
		ctx.lineTo(250, 40);
		ctx.lineTo(20, 150);
		ctx.moveTo(300,200);
		ctx.lineTo(10, 10);
		ctx.lineCap = "round";
//		ctx.lineCap = "square";
		
		ctx.arc(200, 100, 25, 0, (1/4)*Math.PI, true);		// 円を描画する関数
		ctx.arc(150, 200, 50, 0, 2*Math.PI, false);
		
		ctx.stroke();	// 枠線の描画
		ctx.fill();		// 塗りつぶしの描画
	}
}

