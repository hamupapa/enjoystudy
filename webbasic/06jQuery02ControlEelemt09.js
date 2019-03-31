'use strict';

(function($){
	
	$(document).ready(function(){	/* ページが読み込まれたら実行する */
		/* 要素の高さ・横幅を取得する */
		var result1 = $("#element").height();
		var result2 = $("#element").width();
		var result3 = $("#element").css("background-color");
		$("#result1").html(result1);
		$("#result2").html(result2);
		$("#result3").html(result3);
	});
	
})(jQuery);