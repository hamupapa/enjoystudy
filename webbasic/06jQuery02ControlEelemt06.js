'use strict';

(function($){
	
	$(document).ready(function(){	/* ページが読み込まれたら実行する */
		/* 要素にクラスを追加する */
		var contents = $("div:first").html();
		$("#hello").addClass("on");
	});
	
})(jQuery);