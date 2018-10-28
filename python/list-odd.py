#
# 10以下の奇数を持つリストを内方表記で作成
# 2倍して1を足す方法
#
data = [ i*2+1 for i in range(0, 5) ]
print(data)

#
# 10以下の奇数を持つリストを内方表記で作成
# 2倍して1を引く方法
#
data = [ i*2-1 for i in range(1, 6) ]
print(data)

#
# 10以下の奇数を持つリストを内方表記で作成
# range()を工夫する方法
#
data = [ i for i in range(1, 11, 2) ]
print(data)

#
# 10以下の奇数を持つリストを内方表記で作成
# 内包表記でforとifを組み合わせる方法
#
data = [ i for i in range(1, 11) if i % 2 == 1 ]
print(data)
