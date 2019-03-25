'use strict';

(function($){
	
	$(document).ready(function(){	/* ページが読み込まれたら実行する */
		/* JavaScriptでの要素選択 */
		var elem1 = document.getElementById("hello1");
		elem1.style.backgroundColor="#9F9";
		
		/* ID名から要素を取得する */
		var elem2 = $("#hello2");
		elem2.css("backgroundColor", "#9F9");
		
		/* クラス名から要素を取得する */
	});
	
})(jQuery);