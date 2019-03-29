'use strict';

(function($){
	
	$(document).ready(function(){	/* ページが読み込まれたら実行する */
		/* 要素からクラスを削除する */
		var contents = $("div:first").html();
		$("#hello").removeClass("on");
	});
	
})(jQuery);