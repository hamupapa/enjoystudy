#
# tuple
#
print("<tuple：タプル　要素を変更できないリスト>")
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


#
# set
#
print("<set：集合型>")
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


#
# 辞書型
#
print("<辞書型>")
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
