#
# リスト内包表記
#
list_data = [ (x+y) for x in [1, 2, 3] for y in [1, 2, 3] ]
print(list_data)

#
# 集合(set)内包表記
#
set_data = { (x+y) for x in [1, 2, 3] for y in [1, 2, 3] }
print(set_data)

#
# 辞書型内包表記
#
dict_data = { "h"+str(x) : x*5 for x in range(1, 4)}
print(dict_data)

#
# ジェネレータ式
#
# ジェネレータ式でジェネレータを生成
gen_data = (x**2 for x in [1, 2, 3])
for i in gen_data:
    print(i)
