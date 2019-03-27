'use strict';

(function($){
	
	$(document).ready(function(){	/* ページが読み込まれたら実行する */
		/* JavaScriptでの要素選択 */
		var elem1 = document.getElementById("hello1");
		elem1.style.backgroundColor="#9F9";
		
		/* ID名から要素を取得する */
		var elem2 = $("#hello2");
		elem2.css("backgroundColor", "#99F");
		
		/* クラス名から要素を取得する */
		var elem3 = $(".elems");
		elem3.css("backgroundColor", "#F99");
		
		/* タグ名から要素を取得する */
		var elem4 = $("h1");
		elem4.css("backgroundColor", "#999");
		
		/* 最初の要素の選択 */
		var elem5 = $("li:first");
		elem5.css("backgroundColor", "#FF9");
		
		/* 最後の要素の選択 */
		var elem5 = $("li:last");
		elem5.css("backgroundColor", "#9FF");
		
		/* 3番目の要素の選択 */
		var elem5 = $("li:eq(2)");
		elem5.css("backgroundColor", "#99F");
	});
	
})(jQuery);
