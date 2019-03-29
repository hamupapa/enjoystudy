'use strict';

(function($){
	
	$(document).ready(function(){	/* ページが読み込まれたら実行する */
		/* 要素のクラスの切り替え */
		var contents = $("div:first").html();
		$("#hello").toggleClass("on");
		$("#world").toggleClass("on");
	});
	
})(jQuery);