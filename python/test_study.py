# -*- coding: utf-8 -*-

import random

print("================ リストの基本 ================")
# リストの定義
a = [10, 22, 30, 45]
print(a)
print(a[0]) # リストの要素指定(0番目)
print(a[3]) # リストの要素指定(3番目)

# リストの要素を更新
a[1] = 555
print(a)

# リストの要素数を調べる
a = [1, 2, 3, 4, 5, 6, 7]
b = [0, 2, 4, 6]
print(len(a))
print(len(b))

print("================ リストの基本2 ================")
# あるクラスの国語テストの点数をリストに代入
points = [88, 76, 67, 43, 79, 80, 91]

# テストの合計を求める
sum_v = 0
for i in points:
    sum_v += i
    print(i,"点を足して合計は", sum_v)

# 平均を求める
ave_v = sum_v / len(points)
print("平均点は", ave_v, "点")

# テストの合計を求める
sum_v = 0
sum_v = sum(points)     # sum()関数で合計を求める
ave_v = sum_v / len(points)
print("合計点は", sum_v, "点")
print("平均点は", ave_v, "点")


print("================ リストの基本3 ================")
# 文字列でリスト作成
fruits = ["Apple", "Banana", "Mango", "Orange"]
for i in fruits:
    print("「" + i + "」が好き！")

kakugen =  [
    "能ある鷹は爪を隠す",
    "豚に真珠",
    "二兎を追う者は一兎をも得ず",
    "叩き続けなさい。そうすれば開かれます。"]

# ランダムに数値を一つ選ぶ
i = random.randint(0, len(kakugen)-1)

# 選んだ格言を表示する
print(kakugen[i])

# for構文でenumerate()を使う
for i, v in enumerate(fruits):
    print(i, v)

for i, v in enumerate(fruits):
    print("%d番目は%s" % (i, v))


print("================ リストの操作(要素の追加) ================")
# リストを作成
nums = [1, 2, 3]

# append()で値を追加
nums.append(4)
nums.append(5)

# 結果を確認
print(nums)


# 国語の点数の一覧
points = [80, 40, 23, 14, 29, 58]

# 30点未満のデータだけ選んで赤点リストに追加
akaten = []
for p in points:
    if p < 30:
        akaten.append(p)
print(akaten)


#  2つのリストを生成
n1 = [1, 3, 5]
n2 = [2, 4, 6]

# 2つのリストを結合してn3に代入
n3 = n1 + n2
print(n3)

# extend()メソッドを使う方法
b = [11, 22]
b.extend(n1)
print(b)


print("================ リストの操作(スライス) ================")
# リスト[開始:終了]
# リスト[開始:終了:ステップ]
a = [10, 555, 30, 45]
print(a[1:3])

b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(b[1:3])
print(b[1:5])
print(b[:3])    # 先頭(0)を省略
print(b[7:])    # 末尾を省略
print(b[-1])    # 後ろから1つ目
print(b[-2])    # 後ろから2つ目
print(b[-3:])   # 後ろから3つ目から最後まで

print(b[2:8:2])     # 2から8の間を2個目に出てきた値を得る
print(b[::3])       # 最初から最後まで3個目に出てきた値を得る



print("================ リストの操作(要素の削除) ================")
# 特定の要素を削除
# del リスト[要素インデックス]
nums = [0, 1, 2, 3, 4]
del nums[2]
print(nums)

# スライス指定して特定の範囲を削除
nums = [0, 1, 2, 3, 4]
del nums[2:4]
print(nums)

print("================ リストの操作(その他のリスト操作) ================")

# insert(i, x)
# インデックスiの位置にxを挿入する
b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b.insert(5, 10)
print(b)

# remove(x)
# リストの中にある値xを削除する
b = [0, 1, 2, 3, 9, 4, 5, 6, 7, 8, 9]
b.remove(9)
print(b)

# pop()
# リストの末尾にある要素を取り出し削除する
b.pop()
print(b)

# clear()
# リストの全要素を削除
b.clear()
print(b)

# index(x)
# リストから値xを探してその位置(インデックス)を返す
b = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(b.index(12))

# 指定した値がリストになかったら？→エラーになる
#i = b.index(11)

# 指定した値がリストに複数あったら？→最初に見つかったインデックスのみ返される
b = [0, 2, 4, 6, 14, 8, 10, 12, 14, 16, 18]
print(b.index(14))

# count(x)
# リスト中にxが何回出現するか回数を返す
b = [0, 2, 4, 6, 14, 8, 10, 12, 14, 16, 18]
print(b.count(6))
print(b.count(9))
print(b.count(14))

# sort(key, reverse)
# リストを昇順に並べ替える(reverse=Trueで降順)
b = [5,9,1,7,4,8,2,3,6]
b.sort()
print(b)

b = [5,9,1,7,4,8,2,3,6]
b.sort(reverse=True)
print(b)

# copy()
# リストの複製(浅いコピー)を返す
b1 = [0, 1, 2, 3, 9, 4, 5, 6, 7, 8, 9]
b2 = b1.copy()
print(b1)
print(b2)


print("================ タプル(要素を変更できないリスト) ================")
# タプルを作成
a = (10, 20, 30)

# 要素の参照
print(a[1])

# スライス
print(a[:2])

# 値を変更することはできない
#a[1] = 50

# タプルからリストに変換
a_list = list(a)
a_list[1] = 50
print(a_list)

# リストからタプルに変換
a_tuple = tuple(a_list)
#a_tuple[2] = 100



print("================ 集合型 ================")
# 重複する値を持たせることができない
# 順序をつけることができない
# 結合・交差・差分・対象差などの数学的演算を行うことができる

# 集合型を生成
colors = {"red", "green", "blue"}
print(colors)

# 空の集合型を生成
e = set()
print(e)

# set()を使って集合型を生成
fruits = set({"orange", "banana", "mango"})
print(fruits)

# 差分を求める
box1 = {"ハンマー", "釘", "ペンチ"}
box2 = {"釘", "ペンチ"}
print(box1 - box2)

# box3にペンチが入っているかを調べる
box3 = {"ハンマー", "釘", "ペンチ"}
print("ペンチ" in box3)

# 各種演算子
team1 = {"遠藤", "佐藤", "中村"}
team2 = {"田中", "遠藤", "中村"}
team3 = team1 | team2
print(team3)

team4 = team1 & team2
print(team4)



print("================ 辞書型 ================")
# 辞書型データ作成
ages = {"鈴木":30, "井上":20, "伊藤":22}
print(ages)

# 辞書型のデータを参照・設定する方法
# 伊藤さんの年齢参照
print(ages["伊藤"])

# 鈴木さんの年齢を更新
ages["鈴木"] = 29
print(ages)

# キーの存在確認
prices = {"バナナ":300, "りんご":200, "マンゴー":400}
print("りんご" in prices)
print(prices["りんご"])
print("みかん" in prices)

# 要素を列挙する方法
# 辞書型.keys()
# フルーツの価格表を辞書型で定義
prices = {"Banana":300, "Apple":200, "Mango":400}

# キーの一覧取得
print(prices.keys())            # dict_keys型
print(list(prices.keys()))      # リストで取得
print(sorted(prices.keys()))    # ソート済のリストで取得
print(sorted(prices.keys(), reverse = True))    # 降順でソート

# 値の一覧取得
print(prices.values())

# (キー, 値)のタプルのリストで一覧取得
print(prices.items())           # dict_items型
print(list(prices.items()))

# 辞書型とforループの組み合わせ
# 辞書型のデータ(果物名,値段)を変数に代入
fruits = {
    "バナナ":300,
    "オレンジ":240,
    "イチゴ":350,
    "マンゴー":400
    }

# 辞書型のデータ一覧を表示
for name in fruits.keys():
    # 値段を取得
    price = fruits[name]

    # 画面に出力
    s = "{0}は、{1}円です。".format(name, price)
    print(s)


# 辞書型のデータ(果物名と値段)を変数に代入
for name, price in fruits.items():
    # 画面に出力
    s = "{0}は、{1}円です。".format(name, price)
    print(s)

# 変数a, b, cにリストの値を振り分ける
a, b, c = [2, 300, 4000]
print(a, b, c)

# 成績データを辞書型で定義
records = {
    "Tanaka":72, "Yamada":65, "Hirata":100,
    "Akai":56, "Fukuda":66, "Sakai":80
    }

# 合計を求める
sum_v = 0
for v in records.values():
    sum_v += v

# 平均点を計算して結果を表示
ave_v = sum_v / len(records)
print("合計点:", sum_v)
print("平均点:", ave_v)

# 成績データの一覧と平均点との差を表示
fmt = "| {0:<7} | {1:>4} | {2:>5} |"    # 7文字左寄せ、4文字右寄せ、5文字右寄せ指定
print("| 名前    | 点数 | 差")
for name, v in sorted(records.items()):
    # 平均点との差を求める
    diff_v = v - ave_v
    # 小数点以下を丸める
    diff_v = round(diff_v, 1)   # diff_vの値を小数点以下1位になるよう四捨五入
    # 書式に沿って出力
    print(fmt.format(name, v, diff_v))

# 単語の出現回数をカウント
text = """
Keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""

# 単語を区切る
text = text.replace(";", "")    # :を削除
text = text.replace(",", "")    # ,を削除
text = text.replace(".", "")    # .を削除
words = text.split()            # 空白で区切ってリスト型を作成

# 単語を数える
counter = {}    # counterという空の辞書型を作成
for w in words:
    ws = w.lower()    # 小文字に変換
    if ws in counter:   # counterにキーがあれば値をインクリメント
        counter[ws] += 1
    else:               # counterにキーがなければキー登録し値を1にする
        counter[ws] = 1

# 結果を表示
for k, v in sorted(counter.items()):
    if v >= 3:
        print(k, v)




print("================ 文字列の操作(文字列の演算) ================")
# クォート文字列を生成する
s1 = "保つのに時があり捨てるのに時がある"
s2 = '保つのに時があり捨てるのに時がある'
print(s1)
print(s2)

# 三重引用符(トリプルクォート)で文字列を生成
s3 = """捜すのに時があり
あきらめるのに時がある"""
s4 = '''捜すのに時があり
あきらめるのに時がある'''
print(s3)
print(s4)

# 数値から変換する
num = 12345
s5 = str(num)
print(s5)

# 文字列に対する演算
# 2つの文字列を生成
s1 = "abc"
s2 = "def"
# 「+」演算子で結合する
s = s1 + s2
print(s)

# 「*」演算子で指定した数を生成
s = "@"
print(s * 3)
print("love" * 4)

# 文字列の抽出
s = "abcd"
print(s[0])
print(s[2])

# 文字列のスライス
# 文字列を生成
s = "abcdefg"
# 指定した範囲をスライス
print(s[1:4])
print(s[2:3])

n = "0123456789"
print(n[2:5])
print(n[4:9])
print(n[5:8])
print(n[3:3])   # 3文字目から3文字目の手前まで、つまり空文字

print(n[:3])    # 先頭を省略
print(n[7:])    # 末尾を省略

print(n[-1])    # マイナス指定
print(n[-3:])

print(n[0:9:2]) # ステップ指定
print(n[::3])


print("================ 文字列の操作(文字の分割　split()) ================")
# 空白文字で区切り
s = "This is a pen."
print(s.split())

# 区切り文字を指定
s = "2020/02/20"
print(s.split("/"))
print(s.split("/", maxsplit = 1))   # maxsplit=1を指定(一回しか区切られない)


print("================ 文字列の操作(文字の結合　join()) ================")
a = ["aaa", "bbb", "ccc"]

# "連結文字".join(リストなど)
print("-".join(a))

# 文字列を分割
s = "2020/02/20"
a = s.split("/")
print(a)

# 分割したリストを結合
s = "-".join(a)
print(s)


print("================ 文字列の操作(文字の置換 replace()) ================")
s = "This is a pen."
print(s.replace("pen", "note"))
print(s)    # 元の文字列は変わらない



print("================ その他の文字列の操作 ================")
text = """
Keep on asking, and it will be given you;
keep on seeking, and you will find;
keep on knocking, and it will be opened to you;
for everyone asking receives, and everyone seeking finds,
and to everyone knocking, it will be opened.
"""
s = "This is a pen."

# str.find(検索ワード)
# 文字列strのどこに検索ワードがあるか調べる。見つからないときは-1を返す。
print(text.find("seeking"))
print(text.find("aaa"))

# str.lower()
# 文字列strを小文字に変換する
print(s.lower())
print(s)

# str.upper()
# 文字列strを大文字に変換する
print(s.upper())
print(s)

# str.format(v1, v2, ...)
s = "{:04x}".format(255)
print(s)

s = "{0}-{1}-{0}".format("zero", "one")
print(s)

# str.strip([文字集合])
s = "This is a pen."
print(s.strip("e.Tn"))
print(s.strip())

# str.startswith(検索文字 [,開始位置 [, 終了位置]])
s = "This is a pen."
print(s.startswith("T"))
print(s.startswith("This"))
print(s.startswith("That"))
print(s.startswith("T", 1))
print(s.startswith("his", 1))

# str.isnumeric()
# 文字列が数字を表す場合、Trueを返す
print("1".isnumeric())
print("百".isnumeric())
print("a".isnumeric())

print("================ 関数の使い方 ================")
# 入力
#i = input("数字を入力(1回目)")
#add1 = int(i)
add1 = 200
#i = input("数字を入力(2回目)")
#add2 = int(i)
add2 = 562

# 足し算を行う関数を定義
def func_add(a, b):
    ''' 足し算を行う '''
    return a + b

print("{0} + {1} = ".format(add1, add2), end="")
print(func_add(add1, add2))


print("================ lambdaとmapの使い方 ================")
# リストを生成
nums = [1, 3, 5, 7, 9]

# 値を2倍にする無名関数を定義
x2 = lambda x : x * 2

# map()を使ってリストnumsにx2を適用
print(list(map(x2, nums)))

# 無名関数を直書き、かつforループを使って1～5倍する
for i in range(1, 6):
    print(list(map(lambda x : x * i, nums)))


print("================ lambdaとfilterの使い方 ================")
# リストを生成
nums = [1, 2, 3, 11, 12, 13, 21, 22, 23]

# 偶数を抽出する
print(list(filter(lambda x : (x % 2) == 0, nums)))

# 13より大きな値を抽出
print(list(filter(lambda x : x > 13, nums)))

# 8より小さな値を抽出
print(list(filter(lambda x : x < 8, nums)))


print("================ リストや辞書型の値のソート ================")
# (動物, 最高時速)のリスト(各要素はタプルで作成)
animal_list = [
    ("ライオン", 58),
    ("チーター", 110),
    ("シマウマ", 60),
    ("トナカイ",80)
]

# 足の速い順にソート
faster_list = sorted(
    animal_list,
    key = lambda ani : ani[1],
    reverse = True)             # 降順にソート

# 結果を表示
for i in faster_list: print(i)


# 辞書型で動物:最高時速を定義
animal_dict = {
    "ライオン": 58,
    "チーター": 110,
    "シマウマ": 60,
    "トナカイ": 80
}

# 時速でソート
li = sorted(
    animal_dict.items(),
    key = lambda x: x[1],
    reverse = True)

# 結果を表示
for name, speed in li:
    print(name, speed)


print("================ ジェネレータ ================")
# yield で値を返す関数を定義
def genlto3():
    yield 1;
    yield 2;
    yield 3;

# イテレータオブジェクトを得る
it = genlto3()
# for構文で繰り返し表示
for i in it:
    print(i)

# 素数を返すジェネレータ
def genPrime(maxnum):
    num = 2
    while (num < maxnum):
        is_prime = True     # 素数かどうかを管理する変数を定義
        for i in range(2, num): # numが2のときは範囲に含まれる値がなく実行されない
            if(num % i) == 0:   # 素数ではない
                is_prime = False
                break
        if (is_prime):  yield num
        num += 1

# イテレータを得る
it = genPrime(50)

# 画面に出力
for i in it:
    print(i, end=",")

print("\n")
print("================ 例外処理 ================")
# BMI判定(例外処理あり版)
# ユーザーから正しい値を得てBMIを計算
while True:
    try:    # breakするまで繰り返す
        # 入力
        weight = float(input("体重(kg)は?"))
        height = float(input("身長(cm)は?"))
        # BMIの計算
        height = height / 100 # m に直す
        bmi = weight / (height * height)
        break;
    except:
        print("入力ミスがあります。再度入力してください。")

# bmi の値から結果を判定
result = ""
if bmi < 18.5:  result = "痩せ型"
elif bmi < 25:  result = "標準体重"
elif bmi < 30:  result = "肥満(軽)"
else:  result = "肥満(重)"

# 結果を表示
print("BMI :", bmi)
print("判定:", result)


print("================ 特定のエラーだけを補足する ================")
s = input("体重を入力: ")
try:
    v = 100 / float(s)
    print(v)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except:
    print("その他のエラー")


# testtest



