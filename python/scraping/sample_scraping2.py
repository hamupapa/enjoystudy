# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

#r = requests.get('https://news.yahoo.co.jp/')	# ページの情報を取得
r = requests.get('https://www.nikkei.com/')	# ページの情報を取得

#print(r.headers)
#print("------------")
#print(r.encoding)
#print(r.content)

soup = BeautifulSoup(r.content, "html.parser")

try:
	print("1", soup.find("a"))			# 最初のaタグ要素の取得
	print("2", soup.a)					# 最初のaタグ要素の取得
	print("3", soup.find("a").attrs)	# aタグの属性を取得
	print("4", soup.a.attrs)			# aタグの属性を取得
	print("5", soup.a['class'])			# aタグのclassを取得
	print("6", soup.a.name)				# aタグのタグ名を取得
	print("7", soup.a.span)				# aタグの次のpタグを取得
	print("8", soup.a.span.string)		# divタグの次のpタグの内容を取得
except:
	pass


