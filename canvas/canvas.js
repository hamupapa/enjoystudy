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
		ctx2.fillStyle = "#099";		// 文字色
		ctx2.strokeStyle = "#000";		// 縁取り色
		ctx2.lineWidth = 2;				// 縁の太さ
		ctx2.font = "60px serif";		// フォント
		ctx2.fillText("HELLO", 100, 50);		// 文字描画
		ctx2.strokeText("HELLO", 100, 50);		// 縁取り描画
		}
	
}

