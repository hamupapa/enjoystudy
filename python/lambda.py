print("<lambdaとmap>")
# リストを生成
nums = [1, 3, 5, 7, 9]

# 値を2倍にする無名関数を定義
x2 = lambda x : x * 2

# map()を使ってリストnumsにx2を適用
print(list(map(x2, nums)))

# 無名関数を直書き、かつforループを使って1～5倍する
for i in range(1, 6):
    print(list(map(lambda x : x * i, nums)))


print("<lambdaとfilter>")
# リストを生成
nums = [1, 2, 3, 11, 12, 13, 21, 22, 23]

# 偶数を抽出する
print(list(filter(lambda x : (x % 2) == 0, nums)))

# 13より大きな値を抽出
print(list(filter(lambda x : x > 13, nums)))

# 8より小さな値を抽出
print(list(filter(lambda x : x < 8, nums)))


print("<lambdaとsorted>")
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
