import random

#
# リストの基本1
#
print("<リストの基本1>")
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

#
# リストの基本2
#
print("<リストの基本2>")
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


#
# リストの基本3
#
print("<リストの基本3>")
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


#
# リストの操作：要素の追加
#
print("<リストの操作：要素の追加>")
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


#
# リストの操作：スライス
#
print("<リストの操作：スライス>")
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



#
# リストの操作：要素の削除
#
print("<リストの操作：要素の削除>")
# 特定の要素を削除
# del リスト[要素インデックス]
nums = [0, 1, 2, 3, 4]
del nums[2]
print(nums)

# スライス指定して特定の範囲を削除
nums = [0, 1, 2, 3, 4]
del nums[2:4]
print(nums)

#
# リストの操作：その他のリスト操作
#
print("<リストの操作：その他のリスト操作>")

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
