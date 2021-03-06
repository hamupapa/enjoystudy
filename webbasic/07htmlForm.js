'use strict';

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（メールアドレス）
	$("#form1").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result1")
			.children().remove().end()
			.append(inputValues);
	});
});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（電話番号）
	$("#form2").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result2")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（URL）
	$("#form3").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result3")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（数値）
	$("#form4").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result4")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（カラーピッカー）
	$("#form5").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result5")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（日付）
	$("#form6").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result6")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（時間）
	$("#form7").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result7")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（日付時間）
	$("#form8").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result8")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（必須入力チェック）
	$("#form9").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result9")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（最小値/最大値チェック）
	$("#form10").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result10")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（文字数チェック）
	$("#form11").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result11")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（正規表現を使ったチェック/HTML5のみ有効）
	$("#form12").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result12")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（先頭がaで始まる文字のみ有効）
	$("#form13").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result13")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（先頭がaで始まる文字のみ有効(入力チェック無効)）
	$("#form14").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result14")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（名前の入力補助）
	$("#form15").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result15")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（メールアドレスの入力補助）
	$("#form16").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result16")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（電話番号の入力補助）
	$("#form17").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result17")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（郵便番号の入力補助）
	$("#form18").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result18")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（郵便番号の入力補助(無効)）
	$("#form19").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result19")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（読み取り専用）
	$("#form20").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result20")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（プレースホルダー）
	$("#form21").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result21")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（オートフォーカス）
	$("#form22").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result22")
			.children().remove().end()
			.append(inputValues);
	});

});

$(function(){
	// フォームが送信されたときに値を出力するサンプルです。（スペルチェック）
	$("#form23").on("submit", function(e){
		e.preventDefault();
		
		const keyValues = $(this).serialize();
		const inputValues = keyValues.split("&").map((keyValue) => {
			return $("<li>").text(decodeURIComponent(keyValue));
		});
		
		$(".result23")
			.children().remove().end()
			.append(inputValues);
	});

});








