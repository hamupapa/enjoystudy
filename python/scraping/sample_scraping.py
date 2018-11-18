# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

r = requests.get('https://news.yahoo.co.jp/')	# ページの情報を取得

#print(r.headers)
#print("------------")
#print(r.encoding)
#print(r.content)

soup = BeautifulSoup(r.content, "html.parser")

for i in soup.select("p.ttl"):
	print(i.getText())