# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

# ページの情報を取得
r = requests.get('https://www.nikkei.com/markets/kabu/')
soup = BeautifulSoup(r.content, "html.parser")

# span要素を全て検索する
span = soup.find_all("span")

nikkei_heikin = ""  # 初期宣言

with open("nikkei_heikin.cvs", "a") as f:   # 出力ファイルオープン
    writer = csv.writer(f, lineterminator="\n")

    csv_list = []   # csvに記述するレコードを作成
    time_ = datetime.now().strftime("%Y/%m/%d %H:%M:%S") # 時刻取得
    csv_list.append(time_)  # 1カラム目に時刻を記録

    # 全てのspan要素の中からclass="mkc-stock_prices"を検索
    for tag in span:
        # classの設定がされていない要素をtag.get("class").pop(0)が
        # エラーとなるのでtryでエラー回避
        try:
            # tagの中からclass="n"のnの文字列を摘出する。
            # 複数classが設定されている場合があるので
            # get関数は配列で返ってくる。そのため配列の
            # 関数pop(0)で、配列の一番最初を摘出する。
            # <span class="hoge" class="foo"> → ["hoge", "foo"] → hoge
            string_ = tag.get("class").pop(0)

            # 摘出したclassの文字列にmkc-stock_pricesが
            # 設定されているかを調べる
            if string_ in "mkc-stock_prices":
                nikkei_heikin = tag.string	# 文字列の抽出
                break
        except:
            pass

    print(nikkei_heikin)
    csv_list.append(nikkei_heikin)  # 2カラム目に日経平均を記録
    writer.writerow(csv_list)   # csvファイルに出力

