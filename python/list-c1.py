#
# 2～10までの偶数のリストをリスト内包表記なしで作成
#
data = []
for i in range(1, 6):
    data.append(i * 2)
print(data)

#
# 2～10までの偶数のリストをリスト内包表記で作成
#
data = [ i*2 for i in range(1, 6) ]
print(data)

#
# 2～10までの偶数のリストをlambdaとmapで作成
#
data = list(map(lambda x : x*2, range(1, 6)))
print(data)
