# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

r = requests.get('https://news.yahoo.co.jp/')	# ページの情報を取得

#print(r.headers)
#print("------------")
#print(r.encoding)
#print(r.content)

soup = BeautifulSoup(r.content, "html.parser")

print(soup.h1)				# 最初のタグ要素の取得
print(soup.h1.attrs)		# h1タグの属性を取得
print(soup.h1['class'])		# h1タグのclassを取得
print(soup.h1.name)			# h1タグのタグ名を取得
print(soup.p)				# 最初のdivタグを取得
print(soup.div.p)			# divタグの次のpタグを取得
print(soup.div.p.string)	# divタグの次のpタグの内容を取得


