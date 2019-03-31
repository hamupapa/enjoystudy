'use strict';

(function($){
	
	$(document).ready(function(){	/* ページが読み込まれたら実行する */
		/* クリックされたら要素を非表示にする */
		$("#btn1").click( function(){
			$("#element").hide();
		});
		
		/* クリックされたら要素を表示する */
		$("#btn2").click( function(){
			$("#element").show();
		});
		
		/* クリックされたら要素の表示・非表示を切り替える */
		$("#btn3").click( function(){
			$("#element").toggle();
		});
		
		/* クリックされたら要素をフェードアウトさせる */
		$("#btn4").click( function(){
			$("#element").fadeOut();
		});
		
		/* クリックされたら要素をフェードインさせる */
		$("#btn5").click( function(){
			$("#element").fadeIn();
		});
		
		/* クリックされたら要素をアニメーションで非表示にする */
		$("#btn6").click( function(){
			$("#element").slideUp();
		});
		
		/* クリックされたら要素をアニメーション非表示させる */
		$("#btn7").click( function(){
			$("#element").slideDown();
		});
	});
	
})(jQuery);