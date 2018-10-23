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
        #weight = float(input("体重(kg)は?"))
        print("体重(kg)は?")
        weight = float(123)
        #height = float(input("身長(cm)は?"))
        print("身長(cm)は?")
        height = float(50)
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
#s = input("体重を入力: ")
print("体重を入力: ")
s = 50
try:
    v = 100 / float(s)
    print(v)
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except:
    print("その他のエラー")


# forと同じ働きをする関数を自作
def for_func(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            v = next(it)
            callback(v)
        except StopIteration:
            break

# リストの内容をすべて画面に出力
nums = [1,2,3]
for_func(
    nums,                   # リスト
    lambda i : print(i))    # 繰り返す処理

# 辞書型の内容をすべて画面に出力
ages = {"Taro":20, "Jiro":15, "Saburo":18}
for_func(
    ages.items(),            # (キー, 値)のタプルを得る
    lambda n : print(n))    # 繰り返す処理
