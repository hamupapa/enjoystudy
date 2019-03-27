'use strict';

(function($){
	
	$(document).ready(function(){	/* ページが読み込まれたら実行する */
		/* ID名を変更する */
		var id_name = $("p:first").attr("id", "bar");
		$("#result").html( id_name.attr("id") );	// 結果出力用

	});
	
})(jQuery);