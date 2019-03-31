'use strict';

(function($){
	
	$(document).ready(function(){	/* ページが読み込まれたら実行する */
		/* 一度に複数のCSS属性を変更する */
		var params = {
			"background-color": "#C00",
			"height": "250px",
			"width": "400px"
		}
		
		$("#element").css(params);
	});
	
})(jQuery);