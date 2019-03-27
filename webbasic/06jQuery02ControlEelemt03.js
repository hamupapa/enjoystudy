'use strict';

(function($){
	
	$(document).ready(function(){	/* ページが読み込まれたら実行する */
		/* 要素内のHTMLを取得する */
		var contents = $("p:first").html();
		$("#result").html(contents);

	});
	
})(jQuery);