'use strict';

//
// コンソールログを出す
//
var name = "CODEPREP";
console.log('Hello ' + name);

//
// JavaScriptの型
//
/* 文字列 */
var string = "Hello";
console.log(string);

/* 数値 */
var number = 10;
console.log(number);

/* 小数 */
var number = 8.7;
console.log(number);

/* 真偽値 */
var boolean = true;
console.log(boolean);

/* 配列 */
var array = [];		// 配列を定義
array.push('Welcome to CODEPREP');	// 配列に文字列を追加
console.log(array[0]);	// 配列の1番目を出力

/* オブジェクト */
var object = {};	// オブジェクトを定義
object.name = "CODEPREP";	// nameプロパティを追加し、文字列を設定
console.log(object.name);	// nameプロパティを出力

/* null */
var value = null;
console.log(value);

/* undefined */
var value = undefined;
console.log(value);

/* 文字列への変換 */
var value = 10;
var string = value.toString();
console.log(string);
console.log(string === 10);
console.log(string === '10');

/* 数値への変換 */
var value = '10';
var number = parseInt(value, 10);	/* 第1引数=変換したい文字列 第2引数=基数(10進数の場合は10) */

/* 真偽値への変換 */
var value1 = 0;
var boolean1 = Boolean(value1);
console.log(boolean1);	// 0はFalseへ変換される

var value2 = 1;
var boolean2 = Boolean(value2);
console.log(boolean2);

console.log(boolean1 === false);
console.log(boolean2 === true);

//
// 算術演算子
//
/* 足し算 */
var number = 3 + 5;
console.log(number);

/* 引き算 */
var number = 10 - 2;
console.log(number);

/* 掛け算 */
var number = 4 * 2;
console.log(number);

/* 割り算 */
var number = 16 / 2;
console.log(number);

/* 余り */
var number = 17 % 9;
console.log(number);

/* インクリメント演算子 */
var number = 5;
console.log(number);
console.log(++number);		// 加算した後の数字が出力される
console.log(number++);		// 加算する前の数字が出力される
console.log(number);

/* デクリメント演算子 */
var number = 5;
console.log(number);
console.log(--number);		// 減算した後の数字が出力される
console.log(number--);		// 減算する前の数字が出力される
console.log(number);

//
// 「論理演算」と「比較演算」
//
/* 論理AND演算子(&&) */
console.log(true && true);		// true
console.log(false && false);	// false
console.log(true && false);		// false

/* 論理OR演算子(||) */
console.log(true || true);		// true
console.log(false || false);	// false
console.log(true || false);		// true

/* 論理NOT演算子(!) */
console.log(!true);		// false
console.log(!false);	// true

/* 等価演算子(==) */
console.log(10 == 10);		// true
console.log(10 == 1);		// false
console.log(10 == '10');	// true(型変換後に比較するため)

/* 不等価演算子(!=) */
console.log(10 != 10);		// false
console.log(10 != 1);		// true
console.log(10 != '10');	// false(型変換後に比較するため)

/* 厳密等価演算子(===) */
console.log(10 === 10);		// true
console.log(10 === 1);		// false
console.log(10 === '10');	// false

/* 厳密不等価演算子(!==) */
console.log(10 !== 10);		// false
console.log(10 !== 1);		// true
console.log(10 !== '10');	// true

/* 関係演算子(> >= < <=) */
console.log(10 > 1);		// true
console.log(1 > 10);		// false
console.log(10 >= 1);		// true
console.log(10 >= 10);		// true
console.log(1 >= 10);		// false
console.log(10 < 1);		// false
console.log(1 < 10);		// true
console.log(10 <= 1);		// false
console.log(10 <= 10);		// true
console.log(1 <= 10);		// true

//
// 条件分岐と繰り返し
//
/* 条件分岐(if) */
var name = 'CODEPREP';

if(name === 'CODEPREP') {
	console.log('Welcome!');
}

/* 条件分岐(else) */
var name = 'CODE_PREP';

if(name === 'CODEPREP') {
	console.log('Welcome!');
} else {
	console.log('See you later');
}

/* 条件分岐(else if) */
var name = 'codecheck';

if(name === 'CODEPREP') {
	console.log('Welcome!');
} else if(name === 'codecheck') {
	console.log('Looks good!');
} else {
	console.log('See you later');
}

/* 三項演算子 */
var name = 'codecheck';

var value = name === 'CODEPREP' ? 'Welcome!' : 'See you later';
console.log(value);

/* for文による繰り返し処理 */
for(var i=0; i <= 10; i++) {
	console.log(i);
}

//
// 関数
//
/* 関数を定義する, 関数を呼び出す */
function add1() {
	console.log('add()を呼び出しました。');
}
add1();

var hello = function Hello() {
	console.log('Hello world!');
}
hello();

/* 関数に値を渡す */
function add2(a, b) {
	console.log(a + b);
}
add2(3, 5);
add2(10, 3);
add2(100, -5);

/* 関数に値を渡す(callback) */
function calc(a, b, callback) {
	callback(a, b);
}
calc(4, 5, add2);
calc(11, 3, add2);
calc(101, -5, add2);

/* 戻り値を返却する */
function add3(a, b) {
	return a + b;
}
var result = add3(4, 6);
console.log(result);


