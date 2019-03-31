'use strict';

(function($){
	
	$(document).ready(function(){	/* ページが読み込まれたら実行する */
		/* クリックされたら処理を行う */
		$("#elem1").click( function(){
			// 実行回数のカウント
			$("#result1").html( parseInt( $("#result1").html() ) + 1 );
		});
		
		/* マウスカーソルが乗せられたら処理を行う */
		$("#elem2").hover( function(){
			// 実行回数のカウント
			$("#result2").html( parseInt( $("#result2").html() ) + 1 );
		});
		
		/* マウスカーソルが乗せられている間処理を行う */
		$("#elem3").mouseover( function(){
			// 実行回数のカウント
			$("#result3").html( parseInt( $("#result3").html() ) + 1 );
		});
		
		/* 選択されたら処理を行う */
		$("#elem4").focus( function(){
			// 実行回数のカウント
			$("#result4").html( parseInt( $("#result4").html() ) + 1 );
		});
		
		/* キー入力されたら処理を行う */
		$("#elem5").keypress( function(){
			// 実行回数のカウント
			$("#result5").html( parseInt( $("#result5").html() ) + 1 );
		});
	});
	
})(jQuery);