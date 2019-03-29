'use strict';

(function($){
	
	$(document).ready(function(){	/* ページが読み込まれたら実行する */
		/* 複数の要素に対して処理を行う */
		$("p").each(function(){
			$(this).html("Hello World");
		});
	});
	
})(jQuery);