'use strict';

(function($){
	
	$(document).ready(function(){	/* ページが読み込まれたら実行する */
		/* 要素数を取得する */
		var num = $(".elem").length;
		$("#result").html(num);

	});
	
})(jQuery);