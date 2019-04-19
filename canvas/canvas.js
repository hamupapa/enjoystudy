'use strict';

window.onload = function() {
	
	var canvas1 = document.getElementById("sketchbook1");
	if (canvas1 && canvas1.getContext) {
		var ctx1 = canvas1.getContext("2d");
		ctx1.fillStyle = "#00C";
		ctx1.fillRect(20, 20, 150, 80);
		ctx1.strokeRect(0, 0, 90, 125);
		ctx1.clearRect(25, 25, 35, 35);
		
		ctx1.strokeStyle = "#030";	// 枠線の色
		ctx1.lineWidth = 5;			// 枠線の太さ
		ctx1.beginPath();
		ctx1.moveTo(50, 100);
		ctx1.lineTo(250, 40);
		ctx1.lineTo(20, 150);
		ctx1.moveTo(300,200);
		ctx1.lineTo(10, 10);
		ctx1.lineCap = "round";
//		ctx1.lineCap = "square";
		
		ctx1.arc(200, 100, 25, 0, (1/4)*Math.PI, true);		// 円を描画する関数
		ctx1.arc(150, 200, 50, 0, 2*Math.PI, false);
		
		ctx1.stroke();	// 枠線の描画
		ctx1.fill();		// 塗りつぶしの描画
	}
	
	var canvas2 = document.getElementById("sketchbook2");
	if (canvas2 && canvas2.getContext) {
		var ctx2 = canvas2.getContext("2d");
		ctx2.fillStyle = "#099";		// 色
		ctx2.strokeStyle = "#000";		// ふち取りの色
		ctx2.lineWidth = 2;				// ふちの太さ
		ctx2.font = "60px serif";		// フォント
		ctx2.fillText("HELLO", 100, 50);		// 文字描画
		ctx2.strokeText("HELLO", 100, 50);		// ふち取り描画
	}
	
	var canvas3 = document.getElementById("sketchbook3");
	if (canvas3 && canvas3.getContext) {
		var ctx3 = canvas3.getContext("2d");
		ctx3.fillStyle = "#C00";
		ctx3.fillRect(0, 0, 50, 50);	// 矩形
		ctx3.setTransform(1,0,0,1,0,0);	// 伸縮x, 傾斜y, 傾斜x, 伸縮y, 移動x, 移動y
		ctx3.rotate((1/8) * Math.PI);
		ctx3.fillRect(50, 0, 50, 50);
		ctx3.rotate((1/8) * Math.PI);
		ctx3.fillRect(100, 0, 50, 50);
	}
	
	var canvas4 = document.getElementById("sketchbook4");
	if (canvas4 && canvas4.getContext) {
		var ctx4 = canvas4.getContext("2d");
		ctx4.fillStyle = "#0C0";
		ctx4.font = "40px serif";		// フォント
		ctx4.shadowColor = "#333";
		ctx4.shadowOffsetX = -2;
		ctx4.shadowOffsety = 3;
		ctx4.shadowBlur = 5;
		ctx4.fillRect(10, 10, 100, 100);
		ctx4.beginPath();
		ctx4.arc(165, 165, 50, 0, 2*Math.PI, false);
		ctx4.fill();
		ctx4.fillText("TEST TEXT", 220, 50);
	}
	
	var canvas5_1 = document.getElementById("sketchbook5_1");
	if (canvas5_1 && canvas5_1.getContext) {
		var ctx5_1 = canvas5_1.getContext("2d");
		var g1 = ctx5_1.createLinearGradient(0, 0, 100, 0);
		g1.addColorStop(0, "#00F");
		g1.addColorStop(0.3, "#CC0");
		g1.addColorStop(1, "#003");
		ctx5_1.fillStyle = g1;
		ctx5_1.fillRect(0, 0, 300, 300);
		
	}
	
	var canvas5_2 = document.getElementById("sketchbook5_2");
	if (canvas5_2 && canvas5_2.getContext) {
		var ctx5_2 = canvas5_2.getContext("2d");
		var g2 = ctx5_2.createRadialGradient(150, 150, 25, 150, 150, 80);
		g2.addColorStop(0, "#00F");
		g2.addColorStop(0.3, "#CC0");
		g2.addColorStop(1, "#003");
		ctx5_2.fillStyle = g2;
		ctx5_2.fillRect(0, 0, 300, 300);
	}
	
	var canvas6 = document.getElementById("sketchbook6");
	if (canvas6 && canvas6.getContext) {
		
		function move() {
			x += 3;
			y += 2;
			ctx6.fillStyle = "#FFF";
			ctx6.fillRect(0, 0, 500, 300);
			ctx6.fillStyle = "#F00";
			ctx6.fillRect(x, y, 30, 30);
		}
		
		var ctx6 = canvas6.getContext("2d");
		var x = 0, y = 0;
		ctx6.fillStyle = "#F00";
		ctx6.fillRect(x, y, 30, 30);
		setInterval(move, 50);
		
	}
	
}

